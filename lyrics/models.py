from django.db import models
from datetime import datetime

YEAR_CHOICES = []
for year in range(datetime.now().year, 1970, -1):
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
    name = models.CharField(max_length=200,
            help_text=('<strong>Required.</strong> Use the original name, not '
                       'a translated or romanized form.'))
    slug = models.SlugField(max_length=30, unique=True,
            verbose_name='Short name',
            help_text=('<strong>Required.</strong> Short name to use for URL '
                       'lookup. Use only alphanumeric characters.'))

    def __unicode__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=200,
            help_text=('<strong>Required</strong>. Use the original name, '
                       'not a translated or romanized form.'))
    artist = models.ForeignKey('Artist')
    year = models.IntegerField(choices=YEAR_CHOICES,
            verbose_name='Year published')

    def __unicode__(self):
        return u'({0}) {1}'.format(self.year, self.name)

