#!/usr/bin/env bash

if [ "$ENTRY_APP" == "server" ]; then
  python3 -m uvicorn evebot.asgi:application --host 0.0.0.0 --port 8000 --workers 4
elif [ "$ENTRY_APP" == "worker" ]; then
  celery -A evebot worker -l info
elif [ "$ENTRY_APP" == "beat" ]; then
  celery -A evebot beat -l info
elif [ "$ENTRY_APP" == "flower" ]; then
  celery -A evebot flower
else
  echo "No entrypoint specified"
fi