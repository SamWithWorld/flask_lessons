# !/usr/local/bin python3
# coding: utf-8
# @FileName  :routes.py
# @Time      :2022-09-09 16:08
# @Author    :Sam

# 从app包中导入 app这个实例
from app import app

# 2个路由
@app.route('/')
@app.route('/index')
# 1个视图函数
def index():
    return 'Hello World !'

