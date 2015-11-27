from django.test import TestCase
from models import Song, SongBattle

class AlgorithmTestCase(TestCase):

    def setUp(self):
        song = Song(url="https://www.youtube.com/watch?v=2QcCFcaSXCs", name="song 1")
        song.save()
        song = Song(url="https://www.youtube.com/watch?v=p6WJYe6n-l8", name="song 2")
        song.save()
        song = Song(url="https://www.youtube.com/watch?v=VEmM6vVFrao", name="song 3")
        song.save()
        song = Song(url="https://www.youtube.com/watch?v=WtMlB-BEMso", name="song 4")
        song.save()
        song = Song(url="https://www.youtube.com/watch?v=pz8Kp_yELg0", name="song 5")
        song.save()
        song = Song(url="https://www.youtube.com/watch?v=yBv4kWsi4TE", name="song 6")
        song.save()

    def test_song_battle_creation(self):
        song_battle = SongBattle()

