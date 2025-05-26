from lib.db.connection import get_connection # type: ignore

class Author:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name
        if name:
            if not isinstance(name, str) or not name:
                raise ValueError("Name must be a non-empty string")
            self._save()

    def _save(self):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
        self.id = cursor.lastrowid
        db.commit()
        db.close()

    def articles(self):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        articles = cursor.fetchall()
        db.close()
        return articles

    def magazines(self):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("""
            SELECT m.* FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        magazines = cursor.fetchall()
        db.close()
        return magazines

    def add_article(self, magazine, title):
        from lib.models.article import Article
        return Article(title, self, magazine)