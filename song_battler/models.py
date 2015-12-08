from django.db import models
import urlparse

class UserProfile(models.Model):
    ip_address = models.GenericIPAddressField(blank=True,null=True)
    session_key = models.CharField(max_length=128)
    user_type = models.IntegerField(default=1) # 1 for anonymous, 2 for registered
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return "{ ip = " + str(self.ip_address) + ", session_key = " + str(self.session_key) + " }"


class Song(models.Model):

    url = models.URLField()
    song_id = models.CharField(max_length=32)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    name = models.CharField(max_length=256)
    elo = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)

    def save(self, **kwargs):
        if not self.song_id:
            self.song_id = get_youtube_id_from_url(self.url)
        super(Song, self).save(**kwargs)




class SongBattle(models.Model):

    left_song = models.ForeignKey(Song, related_name='left_song')
    right_song = models.ForeignKey(Song, related_name='right_song')
    winner = models.IntegerField(default=-1) # 0 = pass, 1 = left, 2 = right, -1 = not answered
    user = models.ForeignKey(UserProfile) # todo

    def __str__(self):
        return "{ id = " + str(self.id) + ", winnner = " + str(self.winner) + " }"


def get_youtube_id_from_url(url):
    parsed = urlparse.urlparse(url)
    video_id = urlparse.parse_qs(parsed.query)['v']
    return video_id;