import time
import os
from log_watcher import LogFileEventHandler
from detector import detect_anomaly
from database import SQLiteHelper
from alerts import print_alert
from watchdog.observers import Observer

class IncidentHandler(LogFileEventHandler):
    def __init__(self, file_path, db_helper):
        super().__init__(file_path)
        self.db_helper = db_helper

    def on_modified(self, event):
        if os.path.abspath(event.src_path) == os.path.abspath(self.file_path):
            with open(self.file_path, 'r') as f:
                f.seek(self._file_pos)
                for line in f:
                    anomaly = detect_anomaly(line)
                    if anomaly:
#store in database and print alert
                        self.db_helper.insert_incident(anomaly["type"], anomaly["message"])
                        print_alert(anomaly)
                self._file_pos = f.tell()

def main():
    log_path = "sample.log"
    db_helper = SQLiteHelper("incidents.db")
    event_handler = IncidentHandler(log_path, db_helper)
    observer = Observer()
    directory = os.path.dirname(os.path.abspath(log_path))
    observer.schedule(event_handler, directory, recursive=False)
    observer.start()
    print(f"Watching {log_path} for changes...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    db_helper.close()

if __name__ == "__main__":
    main()
