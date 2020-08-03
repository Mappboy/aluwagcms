# ALU Wagtail test CMS
_Notes to future Cameron_

I've added the spatialite capabilites make sure to do so if we need to set that up.
Depending on server will need to install spatialitelib
SPATIALITE_LIBRARY_PATH = '/usr/local/lib/mod_spatialite.dylib'
`https://github.com/malexer/spatialite`

Create a local.py in settings.py don't commit this

Try set this up with poetry and test with zappa.

Create each new system in its own app

Enabling zappa 
pip install django-s3-storage
python manage.py collectstatic --noinput
zappa update dev
zappa manage dev "collectstatic --noinput"