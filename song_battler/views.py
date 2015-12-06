from django.shortcuts import render
import models_helper as mh


def landing_page_view(request):
    songs = mh.get_top_songs()
    return render(request, 'home.html', {'top_songs': songs})


def song_battle_view(request):
    # get song battle
    # song_battle = get_song_battle(request.session.session_key)
    return render(request, 'battle.html', {})
