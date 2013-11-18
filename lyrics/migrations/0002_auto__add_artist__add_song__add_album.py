# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artist'
        db.create_table(u'lyrics_artist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'lyrics', ['Artist'])

        # Adding model 'Song'
        db.create_table(u'lyrics_song', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lyrics.Artist'])),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lyrics.Album'])),
        ))
        db.send_create_signal(u'lyrics', ['Song'])

        # Adding model 'Album'
        db.create_table(u'lyrics_album', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lyrics.Artist'])),
        ))
        db.send_create_signal(u'lyrics', ['Album'])


    def backwards(self, orm):
        # Deleting model 'Artist'
        db.delete_table(u'lyrics_artist')

        # Deleting model 'Song'
        db.delete_table(u'lyrics_song')

        # Deleting model 'Album'
        db.delete_table(u'lyrics_album')


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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['lyrics']