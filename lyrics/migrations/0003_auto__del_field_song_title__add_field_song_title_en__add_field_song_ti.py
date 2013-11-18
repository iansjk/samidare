# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Song.title'
        db.delete_column(u'lyrics_song', 'title')

        # Adding field 'Song.title_en'
        db.add_column(u'lyrics_song', 'title_en',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Song.title_ja'
        db.add_column(u'lyrics_song', 'title_ja',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Song.original'
        db.add_column(u'lyrics_song', 'original',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Song.romanized'
        db.add_column(u'lyrics_song', 'romanized',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Song.translated'
        db.add_column(u'lyrics_song', 'translated',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Song.title'
        db.add_column(u'lyrics_song', 'title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Deleting field 'Song.title_en'
        db.delete_column(u'lyrics_song', 'title_en')

        # Deleting field 'Song.title_ja'
        db.delete_column(u'lyrics_song', 'title_ja')

        # Deleting field 'Song.original'
        db.delete_column(u'lyrics_song', 'original')

        # Deleting field 'Song.romanized'
        db.delete_column(u'lyrics_song', 'romanized')

        # Deleting field 'Song.translated'
        db.delete_column(u'lyrics_song', 'translated')


    models = {
        u'lyrics.album': {
            'Meta': {'object_name': 'Album'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lyrics.Artist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'lyrics.artist': {
            'Meta': {'object_name': 'Artist'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'lyrics.song': {
            'Meta': {'object_name': 'Song'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lyrics.Album']"}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lyrics.Artist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original': ('django.db.models.fields.TextField', [], {}),
            'romanized': ('django.db.models.fields.TextField', [], {}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title_ja': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'translated': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['lyrics']