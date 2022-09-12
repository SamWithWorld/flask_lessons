# !/usr/local/bin python3
# coding: utf-8
# @FileName  :config.py
# @Time      :2022-09-12 10:58
# @Author    :Sam

import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or 'you will never guess'