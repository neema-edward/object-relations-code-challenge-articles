# lib/models/magazine.py
from lib.db.connection import get_connection

class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category
        if name and category:
            if not isinstance(name, str) or not name:
                raise ValueError("Name must be a non-empty string")
            if not isinstance(category, str) or not category:
                raise ValueError("Category must be a non-empty string")
            self._save()

    def _save(self):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self.name, self.category))
        self.id = cursor.lastrowid
        db.commit()
        db.close()

    def articles(self):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        articles = cursor.fetchall()
        db.close()
        return articles

    def contributors(self):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("""
            SELECT a.* FROM authors a
            JOIN articles art ON a.id = art.author_id
            WHERE art.magazine_id = ?
        """, (self.id,))
        authors = cursor.fetchall()
        db.close()
        return authors

    def article_titles(self):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("SELECT title FROM articles WHERE magazine_id = ?", (self.id,))
        titles = [row['title'] for row in cursor.fetchall()]
        db.close()
        return titles