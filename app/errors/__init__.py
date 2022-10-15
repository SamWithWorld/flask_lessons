# !/usr/local/bin python3
# coding: utf-8
# @FileName  :__init__.py.py
# @Time      :2022-10-14 18:46
# @Author    :Sam

from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers
