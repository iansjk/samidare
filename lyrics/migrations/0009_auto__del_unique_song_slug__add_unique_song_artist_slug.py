# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Song', fields ['slug']
        db.delete_unique(u'lyrics_song', ['slug'])

        # Adding unique constraint on 'Song', fields ['artist', 'slug']
        db.create_unique(u'lyrics_song', ['artist_id', 'slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Song', fields ['artist', 'slug']
        db.delete_unique(u'lyrics_song', ['artist_id', 'slug'])

        # Adding unique constraint on 'Song', fields ['slug']
        db.create_unique(u'lyrics_song', ['slug'])


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'lyrics.song': {
            'Meta': {'unique_together': "(('artist', 'slug'),)", 'object_name': 'Song'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lyrics.Album']", 'null': 'True', 'blank': 'True'}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lyrics.Artist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'romanized': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30'}),
            'title_en': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'title_orig': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'translated': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['lyrics']