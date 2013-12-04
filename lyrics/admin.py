from django.contrib import admin
from django.utils.html import escape
from lyrics.models import Song, Artist, Album

class SongAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General information', {
            'fields': ['title_en', 'title_orig', 'artist', 'album'],
        }),
        ('Lyricsheet', {
            'description': escape(
                 'Enter lyricsheet information here. Full HTML is allowed. A '
                 'single newline will be replaced with <br>, and two '
                 'linebreaks will be interpreted as the start of a new '
                 '<p> element. Trailing whitespace (but not leading '
                 'whitespace) will be removed on each line.'),
            'fields': ['original', 'romanized', 'translated'],
        }),
    ]
    list_display = (
        '__unicode__',
        'artist',
        'album',
        'has_romanization',
        'has_translation',
    )


admin.site.register(Song, SongAdmin)
admin.site.register(Artist)
admin.site.register(Album)
