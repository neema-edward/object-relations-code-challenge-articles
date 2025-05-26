import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection

@pytest.fixture
def setup_db():
    db = get_connection()
    db.executescript("DROP TABLE IF EXISTS articles; DROP TABLE IF EXISTS authors; DROP TABLE IF EXISTS magazines;")
    with open('lib/db/schema.sql', 'r') as f:
        db.executescript(f.read())
    db.commit()
    db.close()

def test_article_creation(setup_db):
    author = Author("John Doe")
    magazine = Magazine("Tech Weekly", "Tech")
    article = Article("Tech Trends", author, magazine)
    assert article.id is not None
    assert article.title == "Tech Trends"
    assert article.author.name == "John Doe"
    assert article.magazine.name == "Tech Weekly"