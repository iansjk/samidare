# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Song.title_ja'
        db.delete_column(u'lyrics_song', 'title_ja')

        # Adding field 'Song.title_orig'
        db.add_column(u'lyrics_song', 'title_orig',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding unique constraint on 'Song', fields ['title_en']
        db.create_unique(u'lyrics_song', ['title_en'])

        # Adding field 'Album.year'
        db.add_column(u'lyrics_album', 'year',
                      self.gf('django.db.models.fields.IntegerField')(default=1900),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'Song', fields ['title_en']
        db.delete_unique(u'lyrics_song', ['title_en'])

        # Adding field 'Song.title_ja'
        db.add_column(u'lyrics_song', 'title_ja',
                      self.gf('django.db.models.fields.CharField')(default=1900, max_length=200),
                      keep_default=False)

        # Deleting field 'Song.title_orig'
        db.delete_column(u'lyrics_song', 'title_orig')

        # Deleting field 'Album.year'
        db.delete_column(u'lyrics_album', 'year')


    models = {
        u'lyrics.album': {
            'Meta': {'object_name': 'Album'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lyrics.Artist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
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
            'title_en': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'title_orig': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'translated': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['lyrics']