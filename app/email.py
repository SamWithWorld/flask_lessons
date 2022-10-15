# !/usr/local/bin python3
# coding: utf-8
# @FileName  :emaill.py
# @Time      :2022-10-14 22:41
# @Author    :Sam

from flask_mail import Message
from threading import Thread
from flask import current_app
from app import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body=None):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    # 异步发送电子邮件
    Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()
    # return thr
    # mail.send(msg)
