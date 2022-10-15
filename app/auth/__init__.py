# !/usr/local/bin python3
# coding: utf-8
# @FileName  :__init__.py.py
# @Time      :2022-10-14 22:17
# @Author    :Sam

from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes
