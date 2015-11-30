from django.shortcuts import render


def landing_page_view(request):
    return render(request, 'home.html', {'title': 'Dub Wars'})


def song_battle_view(request):
    # get song battle
    # song_battle = get_song_battle(request.session.session_key)
    return render(request, 'battle.html', {'Dub Wars'})
