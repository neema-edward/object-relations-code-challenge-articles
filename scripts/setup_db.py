from lib.db.connection import get_connection
from lib.db.seed import seed

with open('lib/db/schema.sql', 'r') as f:
    schema = f.read()
db = get_connection()
db.executescript(schema)
db.commit()
seed()
db.close()