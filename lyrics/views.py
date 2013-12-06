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

    # our data is in column-major order (original is a column, romanized is a
    # column, etc.) but we need to write the information in row-major order.
    # rearrange the data and pass it to the context.
    stanzas = []  # will be a list of lists
    original_stanzas = song.original.split('\n\n')
    romanized_stanzas = song.romanized.split('\n\n')
    translated_stanzas = song.translated.split('\n\n')
    for i in range(len(original_stanzas)):
        stanza = []
        stanza.append(original_stanzas[i])
        if song.romanized:
            stanza.append(romanized_stanzas[i])
        if song.translated:
            stanza.append(translated_stanzas[i])
        stanzas.append(stanza)

    context = {
        'song': song,
        'stanzas': stanzas,
    }
    return render(request, 'song.htm', context)
