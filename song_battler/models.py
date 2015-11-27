from django.db import models
from django.contrib.auth.models import User, AnonymousUser


class UserProfile(models.Model):
    ip_address = models.CharField(max_length=24)
    session_key = models.CharField(max_length=128)


class Song(models.Model):

    url = models.URLField()
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    name = models.CharField(max_length=256)


class SongBattle(models.Model):

    left_song = models.ForeignKey(Song, related_name='left_song')
    right_song = models.ForeignKey(Song, related_name='right_song')
    winner = models.IntegerField() # 0 = pass, 1 = left, 2 = right, -1 = not answered
    user = models.ForeignKey(UserProfile) # todo



