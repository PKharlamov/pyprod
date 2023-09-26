#!/usr/bin/env bash

cd /app/
find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
