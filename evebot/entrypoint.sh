#!/usr/bin/env bash

if [ "$ENTRY_APP" == "server" ]; then
  python3 -m uvicorn evebot.asgi:application
elif [ "$ENTRY_APP" == "worker" ]; then
  celery -A evebot worker -l info
elif [ "$ENTRY_APP" == "beat" ]; then
  celery -A evebot beat -l info
elif [ "$ENTRY_APP" == "flower" ]; then
  celery -A evebot flower
else
  echo "No entrypoint specified"
fi