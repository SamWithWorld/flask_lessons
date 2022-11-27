import os
from dotenv import load_dotenv


# 邮箱、百度翻译配置项均在microblog.env中
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, 'microblog.env'))


DATABASE_URI='mysql+pymysql://root:root@127.0.0.1:3306/microblog?charset=utf8'


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or 'you will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or  DATABASE_URI or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 每页显示的帖子数
    POSTS_PER_PAGE = 6

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'false').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # 客户端授权密码

    # 百度翻译
    BD_TRANSLATOR_APPID = os.environ.get('BD_TRANSLATOR_APPID')
    BD_TRANSLATOR_KEY = os.environ.get('BD_TRANSLATOR_KEY')

    # Elasticsearch配置
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    # Redis 配置
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'





