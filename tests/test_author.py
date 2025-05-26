import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.connection import get_connection

@pytest.fixture
def setup_db():
    db = get_connection()
    db.executescript("DROP TABLE IF EXISTS articles; DROP TABLE IF EXISTS authors; DROP TABLE IF EXISTS magazines;")
    with open('lib/db/schema.sql', 'r') as f:
        db.executescript(f.read())
    db.commit()
    db.close()

def test_author_creation(setup_db):
    author = Author("John Doe")
    assert author.id is not None
    assert author.name == "John Doe"

def test_author_articles(setup_db):
    author = Author("John Doe")
    magazine = Magazine("Tech Weekly", "Tech")
    author.add_article(magazine, "Tech Trends")
    articles = author.articles()
    assert len(articles) == 1
    assert articles[0]['title'] == "Tech Trends"