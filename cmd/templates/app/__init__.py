# _*_ coding: utf-8 _*_

__author__ = "{{.Author}}"

from flask import Flask

import os
import logging
from logging.handlers import RotatingFileHandler
import warnings
warnings.filterwarnings('ignore')

from app.extensions import db
from app.filters import authFilter
from app.config import *

def create_app():
    """ 工厂函数 """
    app = Flask(__name__)
    
    register_blueprint(app)
    # register_plugin(app)
    register_filter(app)
    register_logger()

    return app

from app.api.home import home
def register_blueprint(app):
    """ regisger blueprint """

    app.register_blueprint(home, url_prefix='/home')


def register_plugin(app):
    """ register manage.extensions plugins """

    apply_mysql(app)                # 初始化数据库
    


def register_filter(app):
    """ register manage.filters """

    app.before_request(authFilter)


def register_logger(log_dir="./app/logger/logs/"):
    """ register app.logger """

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # basicConfig
    logging.basicConfig()
    # Control werkzeug output
    logger = logging.getLogger('werkzeug')
    logger.setLevel(logging.ERROR)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    file_log_handler = logging.handlers.RotatingFileHandler(log_dir+'flask.log',
                                                            maxBytes=1024 * 1024,
                                                            backupCount=10,
                                                            encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d %(message)s')
    file_log_handler.setFormatter(formatter)
    logger.addHandler(file_log_handler)


def apply_mysql(app):
    """ 初始化 数据库 """

    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{LOCAL_IP}/{DATABASE_NAME}?charset=utf8mb4'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

    db.init_app(app)