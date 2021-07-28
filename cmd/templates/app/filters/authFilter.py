# _*_ coding: utf-8 _*_

# authFilters are use to filter requests by permission or authentication

__author__ = "{{.Author}}"

from flask import request

def authFilter():
    # login apis don't need auth-filter
    if request.path.startswith("/login"):
        return None

    # Other auth-filter logic...    

    return None