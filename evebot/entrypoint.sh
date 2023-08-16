#!/usr/bin/env bash

if [ "$ENVIRONMENT" == "production" ]; then
    python3 -m uvicorn evebot/evebot.asgi:application
else
    python3 manage.py runserver 0.0.0.0:8000
fi