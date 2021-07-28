# _*_ coding: utf-8 _*_

__author__ = "{{.Author}}"

from flask import Blueprint, request, jsonify

import traceback
import logging

from app.extensions import db

home = Blueprint("home", __name__)

@home.route("/greet", methods=["GET"])
def greet():
    return "Hello brandnew-flask!"


@home.route("/getHome", methods=["POST"])
def getHome():
    # parse args
    args = request.json.get('args')
    try:
        # database CRUD code...
        print("Database CRUD")
        res = {"code": 0, "msg": "succ", "data": {}}
    except:
        logging.error(traceback.format_exc())
        db.session.rollback()
        res = {"code": 1}
        
    return jsonify(res)
