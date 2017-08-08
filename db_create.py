# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-08-04 20:15:33
# @title:  create a database

from app import db
from models import BlogPost

# create the database and table
db.create_all()


# insert data to table
db.session.add(BlogPost("Good", "I\' m good."))
db.session.add(BlogPost("Well", "I\' m well."))
db.session.add(BlogPost("Excellent", "I\' m excellent."))
db.session.add(BlogPost("Shell", "Hello from shell."))

# commit the changes
db.session.commit()
