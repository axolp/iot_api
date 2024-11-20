import os
from .settings import *
from .settings import BASE_DIR


#fake komentarz
ALLOWED_HOSTS= ['*']

CSRF_TRUSTED_ORIGINS= [
    'http://*', 
    'https://*',
 ]

DEBUG= False
SECRET_KEY = os.environ['SECRET']
MIDDLEWARE = [
     'django.middleware.security.SecurityMiddleware',
     'whitenoise.middleware.WhiteNoiseMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",

   
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE= 'whitenoise.storage.CompressManifestStaticFilesStorage'
STATIC_ROOT= os.path.join(BASE_DIR, "staticfiles")
