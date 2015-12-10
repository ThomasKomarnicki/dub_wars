from models import UserProfile, SongBattle, Song


def get_song_battle(request, session_key):
    user_profile = get_or_create_user_from_token(request, session_key)
    song_battle_creator = SongBattleCreator(user_profile)
    return song_battle_creator.get_song_battle()


def get_or_create_user_from_token(request, session_key):
    ip = get_client_ip(request)
    obj, created = UserProfile.objects.get_or_create(session_key=session_key, ip_address=ip)
    return obj


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_top_songs():
    #todo
    songs = Song.objects.order_by('wins').all()[:20]
    return songs


class SongBattleCreator:

    def __init__(self, user_profile):
        self.user_profile = user_profile

    def get_song_battle(self):
        # todo, better algorithm than random
        # left_song = get_random_song(session_key)
        # right_song = get_random_song(session_key, left_song.id)
        # song_battle = SongBattle(user=user_profile, left_song=left_song, right_song=right_song)
        # song_battle.save() # save does give it an id
        #
        # return song_battle
        pass

    def get_random_song(session_key, ignore_id=None):
        # get song battles for user
        # pick song that has been used
        queryset = Song.objects.order_by('?')
        if ignore_id:
            queryset = queryset.exclude(id=ignore_id)
        return queryset.first()

