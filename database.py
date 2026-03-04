import sqlite3
from datetime import datetime

class SQLiteHelper:
    def __init__(self, db_path="incidents.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            type TEXT NOT NULL,
            message TEXT NOT NULL
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def insert_incident(self, incident_type, message, timestamp=None):
        if timestamp is None:
            timestamp = datetime.utcnow().isoformat()
        query = '''
        INSERT INTO incidents (timestamp, type, message)
        VALUES (?, ?, ?)
        '''
        self.conn.execute(query, (timestamp, incident_type, message))
        self.conn.commit()

    def close(self):
        self.conn.close()