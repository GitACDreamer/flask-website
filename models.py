# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-08-04 22:14:26
# @title:  PostModels

from app import db

class BlogPost(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return '<title {}>: {}'.format(self.title, self.description)
