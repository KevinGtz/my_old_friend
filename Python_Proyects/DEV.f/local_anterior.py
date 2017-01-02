from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgres_psycopg2', #cambiar a postgres
        'NAME': 'traveleandoladb', #'traveleando'
        'USER': perfil['databases']['user'],
        'PASSWORD': perfil['databases']['password'],
        'HOST': 'localhost',
        'PORT':''
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'