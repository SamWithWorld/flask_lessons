# !/usr/local/bin python3
# coding: utf-8
# @FileName  :mail_tst.py
# @Time      :2022-10-09 21:44
# @Author    :Sam

from flask import render_template
import config,os
from app.email import send_email


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    print("token:",token,'-'*10,os.getenv("MAIL_DEFAULT_SENDER"))
    send_email('[Microblog] Reset Your Password',
               sender=os.getenv("MAIL_DEFAULT_SENDER"),
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt', user=user, token=token),
               html_body=render_template('email/reset_password.html', user=user, token=token))
