import time
import secrets

class Playlist:
    def __init__(self):
        self.songs = []
        self.size = 0

    def validate_playlist(func):
        def wrapper(self):
            if self.size > 0:
                func(self)
            else:
                print('There is no more songs to listen on the playlist')
        return wrapper

    def add_song(self, song: str):
        if isinstance(song, str):
            self.songs.insert(0, song)
            self.size += 1
        else:
            print('Only strings accepted')

    def listen_all_playlist(self):
        while self.size > 0:
            self.listen_song()

    @validate_playlist
    def listen_song(self):
        song = self.songs.pop()
        self.size -= 1
        print(f'Listening {song}...')
        time.sleep(10)

    @validate_playlist
    def shuffle(self):
        song = secrets.choice(self.songs)
        self.songs.remove(song)
        self.size -= 1
        print(f'Listening {song}...')
        time.sleep(10)