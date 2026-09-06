class Song:
    # Class attributes - shared by all Song instances
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        # Instance attributes - unique to each song
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Call all class methods to update global stats
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        """Increment total song count by 1"""
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        """Add genre to the genres set (automatically prevents duplicates)"""
        cls.genres.add(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        """Add artist to the artists set (automatically prevents duplicates)"""
        cls.artists.add(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        """Update genre_count dictionary - increment if exists, create if new"""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        """Update artist_count dictionary - increment if exists, create if new"""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
