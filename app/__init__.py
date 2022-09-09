# !/usr/local/bin python3
# coding: utf-8
# @FileName  :__init__.py.py
# @Time      :2022-09-09 16:06
# @Author    :Sam

from flask import Flask

app = Flask(__name__)

from app import routes