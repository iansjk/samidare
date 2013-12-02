from django.contrib import admin
from lyrics.models import Song, Artist, Album

class SongAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General information',
                {'fields': ['title_en', 'title_orig', 'artist', 'album']}
        ),
        ('Lyricsheet',
                {'fields': ['original', 'romanized', 'translated']}
        ),
    ]
    list_display = (
        '__unicode__',  # title_orig if it exists, title_en otherwise
        'artist',
        'album',
        'has_romanization',
        'has_translation',
    )


admin.site.register(Song, SongAdmin)
admin.site.register(Artist)
admin.site.register(Album)
