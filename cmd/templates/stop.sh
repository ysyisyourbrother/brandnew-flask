#!/bin/bash

echo "killing gunicorn_{{.Name}}"
killall -9 gunicorn_{{.Name}}