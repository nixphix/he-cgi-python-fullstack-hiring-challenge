#!/bin/sh

echo 'Creating superuser'
/superuser.sh
echo 'Starting Development server'
python manage.py runserver_plus 0.0.0.0:8000
