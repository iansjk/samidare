from django.shortcuts import render, get_object_or_404
from lyrics.models import Song, Artist

def index(request):
    artists = Artist.objects.all()
    context = {'artists': artists}
    return render(request, 'index.htm', context)

def artist(request, artist_slug):
    artist = get_object_or_404(Artist, slug=artist_slug)
    songs = Song.objects.filter(artist=artist)
    context = {
        'artist': artist,
        'songs': songs
    }
    return render(request, 'artist.htm', context)

def song(request, artist_slug, song_slug):
    song = get_object_or_404(Song, artist__slug=artist_slug, slug=song_slug)
    context = {'song': song}
    return render(request, 'song.htm', context)
