from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from lyrics.models import Song, Artist, Album

def index(response):
    return HttpResponse('Nothing here but us trees!')

def artist(response, artist_slug):
    artist = get_object_or_404(Artist, slug=artist_slug)
    return HttpResponse('Found artist: {0}'.format(artist))

def song(response, artist_slug, song_slug):
    song = get_object_or_404(Song, artist__slug=artist_slug, slug=song_slug)
    return HttpResponse('Found song: {0}'.format(song))
