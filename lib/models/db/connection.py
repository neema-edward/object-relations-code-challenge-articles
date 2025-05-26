import sqlite3

def get_connection():
    db = sqlite3.connect('articles.db')
    db.row_factory = sqlite3.Row
    return db