#!/usr/bin/env bash

if [ "$ENTRY_APP" == "server" ]; then
  python3 -m uvicorn evebot.asgi:application --host 0.0.0.0 --port 8000 --workers 4
elif [ "$ENTRY_APP" == "worker" ]; then
  celery -A evebot worker -l info -P eventlet -c 100 -Q celery
elif [ "$ENTRY_APP" == "beat" ]; then
  celery -A evebot beat -l info
elif [ "$ENTRY_APP" == "flower" ]; then
  celery -A evebot flower --url_prefix=/flower --port=5555
else
  echo "No entrypoint specified"
fi