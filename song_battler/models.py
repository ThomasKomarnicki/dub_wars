from django.db import models


class UserProfile(models.Model):
    ip_address = models.GenericIPAddressField()
    session_key = models.CharField(max_length=128)
    user_type = models.IntegerField() # 1 for anonymous, 2 for registered
    email = models.EmailField()
    password = models.CharField(max_length=128)



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



