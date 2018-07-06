#-*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, \
     check_password_hash


db=SQLAlchemy()

class User(db.Model):
     __tablename__ = 'users'
     id = db.Column(db.String(45),primary_key=True)
     username = db.Column(db.String(255),unique=True)
     password = db.Column(db.String(255))
     posts = db.relationship(
          'Post',backref='users',lazy='dynamic')

     def __init__(self,id,username,password):
          self.id = id
          self.username = username
          self.password = password


     def __repr__(self):
          return '<Model User "{}">' .format(self.name)


###添加多对多关系的关联表posts_tags
posts_tags = db.Table('posts_tags',
    db.Column('post_id', db.String(45), db.ForeignKey('posts.id')),
    db.Column('tag_id', db.String(45), db.ForeignKey('tags.id')))

class Post(db.Model):
     """Represents Proected posts."""
     __tablename__ = 'posts'
     id = db.Column(db.String(45),primary_key=True)
     title = db.Column(db.String(255))
     text = db.Column(db.Text())
     publish_date = db.Column(db.DateTime)
     user_id = db.Column(db.String(45),db.ForeignKey('users.id'))
     comments = db.relationship(
          'Comment',backref='posts',lazy='dynamic'
     )
     tags = db.relationship(
          'Tag',secondary=posts_tags,backref=db.backref('posts',lazy='dynamic'))

     def __init__(self,id,title):
         self.id = id
         self.title = title

     def __repr__(self):
          return "<Model Post '{}'>".format(self.title)

class Comment(db.Model):
     """Represents Proected comments."""
     __tablename__='comments'
     id = db.Column(db.String(45),primary_key=True)
     name = db.Column(db.String(255))
     text = db.Column(db.Text())
     date = db.Column(db.DateTime())
     post_id = db.Column(db.String(45),db.ForeignKey('posts.id'))

     def __init__(self,id,name):
          self.id = id
          self.name = name

     def __repr__(self):
          return "<Model Comment '{}'>".format(self.name)

class Tag(db.Model):
     """Trpresents Proected tags."""
     __tablename__ = 'tags'
     id = db.Column(db.String(45),primary_key=True)
     name = db.Column(db.String(255))

     def __init__(self,id,name):
          self.id = id
          self.name = name

     def __repr__(self):
          return "<Model Tag '{}'>".format(self.name)