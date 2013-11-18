from django.db import models
from datetime import datetime

YEAR_CHOICES = []
for year in range(datetime.now().year, 1900, -1):
    YEAR_CHOICES.append((year, year))

class Song(models.Model):
    title_en = models.CharField(max_length=200, unique=True,
            verbose_name='Title (English)',
            help_text=('<strong>Required.</strong> The title translated '
                       'into English, or if the original title if it is '
                       'already in English.'))
    title_orig = models.CharField(max_length=200, blank=True,
            verbose_name='Title (original)',
            help_text='Optional. The original title, if applicable.')

    artist = models.ForeignKey('Artist')
    album = models.ForeignKey('Album')

    original = models.TextField(blank=True, verbose_name='Original lyrics')
    romanized = models.TextField(blank=True, verbose_name='Romanized lyrics')
    translated = models.TextField(blank=True, verbose_name='Translation')

    def __unicode__(self):
        return self.title_orig if self.title_orig else self.title_en

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist')
    year = models.IntegerField(choices=YEAR_CHOICES)

    def __unicode__(self):
        return '(%d) %s' % (self.year, self.name)

