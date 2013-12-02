from django.conf.urls import patterns, url
from lyrics import views

urlpatterns = patterns('',
    # ../lyrics/
    url(r'^$', views.index, name='index'),
    # ../lyrics/<artist-slug>
    url(r'^(?P<artist_slug>[a-z0-9\-]+)$', views.artist, name="artist"),
    # ../lyrics/<artist-slug>/<song-slug>
    url(r'^(?P<artist_slug>[a-z0-9\-]+)/(?P<song_slug>[a-z0-9\-]+)$',
        views.song, name="song"),
)
