# _*_ coding: utf-8 _*_

# Data Access object for table User

__author__ = "{{.Author}}"

from app.models import User
from app.extensions import db

class UserDao():
    @staticmethod
    def add_user(kwargs):
        u = User(id = kwargs["id"], 
                 gender = kwargs["gender"], 
                 provice = kwargs["province"], 
                 city = kwargs["city"])
        db.session.add(u)
    
    # Other Dao methods...