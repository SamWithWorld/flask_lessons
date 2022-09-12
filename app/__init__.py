# !/usr/local/bin python3
# coding: utf-8
# @FileName  :__init__.py.py
# @Time      :2022-09-09 16:06
# @Author    :Sam

from flask import Flask
# 从config模块导入Config类
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes