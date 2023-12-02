#!/bin/bash
status=$?
if [ $status != 0 ]; then
  python manage.py migrate
fi
python manage.py loadall
exec "$@"