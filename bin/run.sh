#!/usr/bin/env bash

echo "Attempting migrations ..."
python /djangodocker/manage.py migrate --noinput

echo "Starting server ..."
python /djangodocker/manage.py runserver 0.0.0.0:8000
