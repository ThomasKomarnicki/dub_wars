from django.db import models


class Song(models.Model):

    url = models.URLField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    name = models.CharField()


class SongBattle(models.Model):

    left_song = models.ForeignKey(Song)
    right_song = models.ForeignKey(Song)
    winner = models.IntegerField() # 0 = pass, 1 = left, 2 = right
    user = models.ForeignKey # todo