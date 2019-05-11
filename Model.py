from Database import Database

class Model:
    def __init__(self):
        self.db = Database()

    def songName(self):
        for res in self.song:
            name = res[0]
        return name

    def artistName(self):
        for res in self.song:
            artist = res[1]
        return artist

    def level(self):
        for res in self.song:
            level = res[2]
        return level

    def mode(self):
        for res in self.song:
            mode = res[3]
        return mode

    def random(self):
        self.song = self.db.query("SELECT Name, Artist, Level, Mode FROM justdance ORDER BY RAND() LIMIT 1")
        return self.song

    def __str__(self):
        return self.song




m = Model()
print(m.random())


