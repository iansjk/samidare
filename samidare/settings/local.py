from .base import *

SECRET_KEY = 'ars7*os5oqu$j-8llrtqbysek)3@2t6s_@uhpmn#yl9embzkd%'

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'samidare',
        'USER': 'samidare',
        'PASSWORD': 'mayshowers',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
