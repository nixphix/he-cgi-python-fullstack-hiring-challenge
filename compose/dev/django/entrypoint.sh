#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

echo 'Running migrations' &&
# python /app/manage.py makemigrations &&
python /app/manage.py migrate &&
echo 'Collecting static files' &&
python /app/manage.py collectstatic --noinput &&
echo 'Starting nginx server' &&
nginx &&
exec "$@"
