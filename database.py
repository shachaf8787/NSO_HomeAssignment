import sqlite3


class Database:
    """Class to manage database. Add message, get message, delete message"""
    
    def __init__(self):
        self.conn = sqlite3.connect('messages.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS messages
            (application_id text, session_id text, message_id text, participants text, content text)''')

    def add_message(self, application_id, session_id, message_id, participants, content):
        """Add message to database"""
        self.c.execute("INSERT INTO messages VALUES (?, ?, ?, ?, ?)",
                    (application_id, session_id, message_id, participants, content))
        self.conn.commit()

    def get_message(self, application_id, session_id, message_id):
        """Get message from database"""
        self.c.execute("SELECT * FROM messages WHERE application_id=? AND session_id=? AND message_id=?",
                    (application_id, session_id, message_id))
        return self.c.fetchone()

    def delete_message(self, application_id, session_id, message_id):
        """Delete message from database"""
        self.c.execute("DELETE FROM messages WHERE application_id=? AND session_id=? AND message_id=?",
                    (application_id, session_id, message_id))
        self.conn.commit()