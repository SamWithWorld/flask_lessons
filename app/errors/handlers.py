# !/usr/local/bin python3
# coding: utf-8
# @FileName  :handlers.py
# @Time      :2022-10-03 21:17
# @Author    :Sam

from flask import render_template
from app import db
from app.errors import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500
