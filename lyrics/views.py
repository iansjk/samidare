from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse('Nothing here but us trees!')

def artist(response, artist_slug):
    return HttpResponse('Artist slug: "{0}"'.format(artist_slug))

def song(response, artist_slug, song_slug):
    return HttpResponse('Artist slug: "{0}", Song slug: "{1}"'.format(
        artist_slug, song_slug))
