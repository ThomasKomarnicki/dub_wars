from models import UserProfile, SongBattle, Song


def get_song_battle(session_key):
    user_profile = get_user_from_token(session_key)
    # todo, better algorithm than random
    left_song = get_random_song()
    right_song = get_random_song(left_song.id)
    song_battle = SongBattle(user=user_profile, left_song=left_song, right_song=right_song)
    song_battle.save() # save does give it an id
    return song_battle


def get_user_from_token(session_key):
    return UserProfile.objects.get(session_key=session_key)


def get_random_song(ignore_id = None):
    queryset = Song.objects.order_by('?')
    if ignore_id:
        queryset = queryset.exclude(id=ignore_id)
    return queryset.first()