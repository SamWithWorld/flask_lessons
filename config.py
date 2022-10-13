import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))  # 获取当前.py文件的绝对路径

'''通过dotenv管理配置项（目前不采用此方法），前提：分别执行export 命令，例如export MAIL_SERVER='smtp.163.com'；export MAIL_PORT=25等'''
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, 'microblog.env'))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or 'you will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 每页显示的帖子数
    POSTS_PER_PAGE = 3

    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USERNAME = '<你的163邮箱地址>'
    MAIL_PASSWORD = '<你的163邮箱密码>'
    MAIL_DEFAULT_SENDER = '<你的163邮箱地址>'

    # 百度翻译

    BD_TRANSLATOR_APPID = os.environ.get('BD_TRANSLATOR_APPID')

    BD_TRANSLATOR_KEY = os.environ.get('BD_TRANSLATOR_KEY')



