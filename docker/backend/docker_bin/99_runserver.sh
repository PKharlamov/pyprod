#!/usr/bin/env bash

ls -la
pwd

if [ $# -eq 0 ]
then
  cd app
  uvicorn main:app --host 0.0.0.0 --port 8000 --workers 1 --reload
else
  exec "$@"
fi
