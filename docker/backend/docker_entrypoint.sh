#!/usr/bin/env bash

for f in /docker_bin/*; do
    ${f} "$@"
done
