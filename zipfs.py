
class Song(object):

    def __init__(self, frequeny, name, seq):
        self.frequeny = frequeny
        self.name = name
        self.quality = frequeny * seq

    def get_name(self):
        return self.name


class Album(object):

    def __init__(self):
        self.album = []

    def add_song(self, song):
        self.album.append(song)

    def get_album(self):
        return self.album

    def sort_by_quality(self, m):
        songs = self.album
        songs.sort(key=lambda x: x.quality, reverse=True)
        for i in songs[:m]:
            print i.get_name()



NM = raw_input()
N, M = map(int, NM.strip().split(" "))

album = Album()
for i in range(N):
    song = raw_input()
    song = song.strip().split(" ")
    s = Song(int(song[0]), song[1], i+1)
    album.add_song(s)

album.sort_by_quality(M)




