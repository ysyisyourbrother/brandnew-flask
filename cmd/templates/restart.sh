#!/bin/bash

echo "killing gunicorn_{{.Name}}"
killall -9 gunicorn_{{.Name}}

mkdir -p /tmp/bin/
cp /usr/local/bin/gunicorn /tmp/bin/gunicorn_{{.Name}}

echo "restart gunicorn_{{.Name}}"
/tmp/bin/gunicorn_{{.Name}} -c gunicorn_conf.py main:app --daemon
