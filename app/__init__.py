# !/usr/local/bin python3
# coding: utf-8
# @FileName  :__init__.py.py
# @Time      :2022-09-09 16:06
# @Author    :Sam

from flask import Flask
# 从config模块导入Config类
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

db = SQLAlchemy(app)  # 数据库对象
migrate = Migrate(app,db)  # 迁移引擎对象

app.config.from_object(Config)

from app import routes, models  # 导入一个新模块models，它将定义数据库的结构
