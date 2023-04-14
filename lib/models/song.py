from lib import CONN, CURSOR

class Song:

    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS songs (
        id INTEGER PRIMARY KEY,
        name TEXT,
        artist TEXT,
        fav TEXT
        )
        """
        CURSOR.execute(sql)

    def __init__(self, name, artist, fav, id = None):
        self.name = name
        self.artist = artist
        self.fav = fav
        self.id = id

    def create(self):
        sql = """INSERT INTO songs (name, artist, fav)
        VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, [self.name, self.artist, self.fav])
        CONN.commit()
        self.id = CURSOR.execute("SELECT id FROM songs ORDER BY id DESC").fetchone()[0]