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
# 初始化Flask-Login
from flask_login import LoginManager
from logging.handlers import RotatingFileHandler
import os, logging

app = Flask(__name__)

db = SQLAlchemy(app)  # 数据库对象
migrate = Migrate(app, db)  # 迁移引擎对象
login = LoginManager(app)
login.login_view = 'login'

app.config.from_object(Config)

from app import routes, models, errors  # 导入一个新模块models，它将定义数据库的结构

if not app.debug:

    if not os.path.exists('logs'):
        os.mkdir('logs')

    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')
