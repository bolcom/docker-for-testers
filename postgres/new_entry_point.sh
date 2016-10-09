#!/bin/bash -eux

if [ "$1" = 'postgres' ]; then
    exec gosu postgres "$@"
else
    exec "$@"
fi