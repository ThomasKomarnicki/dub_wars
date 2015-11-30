from models import UserProfile, SongBattle, Song


def get_song_battle(request, session_key):
    user_profile = get_or_create_user_from_token(request, session_key)
    print str(user_profile)
    # todo, better algorithm than random
    left_song = get_random_song()
    right_song = get_random_song(left_song.id)
    song_battle = SongBattle(user=user_profile, left_song=left_song, right_song=right_song)
    song_battle.save() # save does give it an id
    return song_battle


def get_or_create_user_from_token(request, session_key):
    ip = get_client_ip(request)
    obj, created = UserProfile.objects.get_or_create(session_key=session_key, ip_address=ip)
    return obj


def get_random_song(ignore_id=None):
    queryset = Song.objects.order_by('?')
    if ignore_id:
        queryset = queryset.exclude(id=ignore_id)
    return queryset.first()


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip