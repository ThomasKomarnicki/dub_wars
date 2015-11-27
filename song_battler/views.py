from django.shortcuts import render
from django.http import HttpResponse
from models import SongBattle
from models_helper import *


def landing_page_view(request):
    return HttpResponse('<h1> Landing Page </h1>')


def song_battle_view(request):
    # get song battle
    song_battle = get_song_battle(request.session.session_key)
