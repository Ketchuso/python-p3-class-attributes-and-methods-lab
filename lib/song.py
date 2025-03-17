class Song:
    all = []
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name 
        self.artist = artist
        self.genre = genre

        Song.all.append(self)
        self.add_song_to_count()
        self.add_to_genres(self.genre)
        self.add_to_artists(self.artist)
        self.add_to_genre_count(self.genre)
        self.add_to_artist_count(self.artist)
    
    @classmethod
    def add_song_to_all(cls, song):
        cls.all.append(song)
    
    def add_song_to_count(self):
        Song.count += 1
    
    def add_to_genres(self, genre):
        if not genre in Song.genres:
            Song.genres.append(genre)
    
    def add_to_artists(self, artist):
        if not artist in Song.artists:
            Song.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1