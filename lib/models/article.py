# lib/models/article.py
from lib.db.connection import get_connection # type: ignore

class Article:
    def __init__(self, title, author, magazine, id=None):
        self.id = id
        self.title = title
        self.author = author
        self.magazine = magazine
        if title and author and magazine:
            if not isinstance(title, str) or not title:
                raise ValueError("Title must be a non-empty string")
            if not hasattr(author, 'id') or not author.id:
                raise ValueError("Author must have an ID")
            if not hasattr(magazine, 'id') or not magazine.id:
                raise ValueError("Magazine must have an ID")
            self._save()

    def _save(self):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
            (self.title, self.author.id, self.magazine.id)
        )
        self.id = cursor.lastrowid
        db.commit()
        db.close()

