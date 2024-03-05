class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        # Increment count of songs and add song to count
        Song.add_song_to_count()
        # Add genre and artist to respective lists
        self.add_to_genres()
        self.add_to_artists()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        if self.genre_count.get(self.genre) is None:
            self.genre_count[self.genre] = 1
        else:
            self.genre_count[self.genre] += 1

        if self.genre not in self.genres:
            self.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist_count.get(self.artist) is None:
            self.artist_count[self.artist] = 1
        else:
            self.artist_count[self.artist] += 1

        if self.artist not in self.artists:
            self.artists.append(self.artist)

# Example usage
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
print(ninety_nine_problems.name)   
print(ninety_nine_problems.artist) 
print(ninety_nine_problems.genre)  

# Accessing class attributes
print(Song.count)       
print(Song.genres)     
print(Song.artists)     
print(Song.genre_count) 
print(Song.artist_count) 
