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
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel
from elasticsearch import Elasticsearch

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()  # 初始化Flask-Login
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'
# 邮件
mail = Mail()
bootstrap = Bootstrap()
moment = Moment()
babel = Babel()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)  # 数据库对象
    migrate.init_app(app, db)  # 迁移引擎对象
    login.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    # 日期和时间
    moment.init_app(app)
    # 翻译
    babel.init_app(app)

    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

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

    return app


from app import models  # 导入一个新模块models，它将定义数据库的结构
