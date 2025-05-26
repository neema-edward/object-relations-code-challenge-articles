from lib.db.connection import get_connection

def seed():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO authors (name) VALUES ('Jane Doe')")
    cursor.execute("INSERT INTO authors (name) VALUES ('John Smith')")
    cursor.execute("INSERT INTO magazines (name, category) VALUES ('Tech Weekly', 'Tech')")
    cursor.execute("INSERT INTO magazines (name, category) VALUES ('News Daily', 'News')")
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('Tech Trends', 1, 1)")
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('AI Revolution', 1, 1)")
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('World Events', 2, 2)")
    db.commit()
    db.close()