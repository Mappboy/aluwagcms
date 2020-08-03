from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+)9wz)$7!h$ojwsi*6g)wua60v4k$r561oyexhd#m7el@*#eo7'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*', 'pj2tp2ufae.execute-api.eu-west-2.amazonaws.com/dev']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
