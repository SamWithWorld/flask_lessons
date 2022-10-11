# !/usr/local/bin python3
# coding: utf-8
# @FileName  :mail_tst.py
# @Time      :2022-10-09 21:44
# @Author    :Sam

from flask import render_template
from flask_mail import Message
from app import mail
import config
from threading import Thread
from app import app


# sys.setdefaultencoding("utf-8")

# 异步发送电子邮件
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body=None):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    # 异步发送电子邮件
    thr = Thread(target=send_async_email, args=(app, msg))
    thr.start()
    return thr
    # mail.send(msg)


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
               sender=config.Config.MAIL_USERNAME,
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt', user=user, token=token),
               html_body=render_template('email/reset_password.html', user=user, token=token))
