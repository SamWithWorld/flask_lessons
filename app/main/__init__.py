# !/usr/local/bin python3
# coding: utf-8
# @FileName  :__init__.py.py
# @Time      :2022-10-14 23:10
# @Author    :Sam

from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes
