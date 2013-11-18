from django.contrib import admin
from .models import Song, Artist, Album

for model in [Song, Artist, Album]:
    admin.site.register(model)

