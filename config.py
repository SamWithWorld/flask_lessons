# !/usr/local/bin python3
# coding: utf-8
# @FileName  :config.py
# @Time      :2022-09-07 04:59
# @Author    :Sam

SECRET_KEY = '3c43135b-6c84-46cd-a9a9-8c84153291ca'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 数据库配置信息
DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_DATABASE = 'flask_book_blog'
DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
