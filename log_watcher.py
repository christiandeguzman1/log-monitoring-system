import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class LogFileEventHandler(FileSystemEventHandler):
    def __init__(self, file_path):
        self.file_path = file_path
#start at the end of the file
        try:
            with open(self.file_path, 'r') as f:
                f.seek(0, 2)
                self._file_pos = f.tell()
        except FileNotFoundError:
            self._file_pos = 0

    def on_modified(self, event):
        if event.src_path == self.file_path:
            with open(self.file_path, 'r') as f:
                f.seek(self._file_pos)
                for line in f:
                    print(line, end='')
                self._file_pos = f.tell()

class LogWatcher:
    def __init__(self, log_path):
        self.log_path = log_path
        self.event_handler = LogFileEventHandler(self.log_path)
        self.observer = Observer()

    def start(self):
        import os
        directory = os.path.dirname(os.path.abspath(self.log_path))
        self.observer.schedule(self.event_handler, directory, recursive=False)
        self.observer.start()
        print(f"Watching {self.log_path} for changes...")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

#example usage:
#if __name__ == "__main__":
#watcher = LogWatcher("sample.log")
#watcher.start()
