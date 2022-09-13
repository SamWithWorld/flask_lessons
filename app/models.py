# !/usr/local/bin python3
# coding: utf-8
# @FileName  :models.py
# @Time      :2022-09-12 21:24
# @Author    :Sam

from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post',backref='author',lazy='dynamic')

    def __repr__(self):
        return '<User %s>' % self.username

class Post(db.Model):
    __tablename__ ='post'
    id = db.Column(db.Integer,primary_key=True)
    body =db.Column(db.String(140))
    timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)