# _*_ coding: utf-8 _*_

# Gunicorn Configuration File

__author__ = "{{.Author}}"

# IP Port
bind = "0.0.0.0:8080"

# Auto reload when code is changed
reload = True

# Concurrency
workers = 4
threads = 4

# HTTPS
# certfile = ""
# keyfile = ""

