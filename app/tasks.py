# !/usr/local/bin python3
# coding: utf-8
# @FileName  :tasks.py
# @Time      :2022/11/26 07:51
# @Author    :Sam

import time, json
from rq import get_current_job
from app import create_app
from app import db
from app.models import Task, User, Post
import sys, os
from flask import render_template
from app.email import send_email

# 添加Flask应用实例和应用上下文
app = create_app()
app.app_context().push()

import requests


def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())


def example(seconds):
    job = get_current_job()
    print('Starting task')
    for i in range(seconds):
        job.meta['progress'] = 100.0 * i / seconds
        job.save_meta()
        print(i)
        time.sleep(1)
    job.meta['progress'] = 100
    job.save_meta()
    print('Task completed')


# 设置任务进度
def _set_task_progress(progress):
    job = get_current_job()
    if job:
        job.meta['progress'] = progress
        job.save_meta()
        task = Task.query.get(job.get_id())
        task.user.add_notification('task_progress', {'task_id': job.get_id(),
                                                     'progress': progress})
        if progress >= 100:
            task.complete = True
        db.session.commit()


# 导出帖子
def export_posts(user_id):
    try:
        # read user posts from database
        user = User.query.get(user_id)
        _set_task_progress(0)
        data = []
        i = 0
        total_posts = user.posts.count()
        for post in user.posts.order_by(Post.timestamp.asc()):
            data.append({'body': post.body,
                         'timestamp': post.timestamp.isoformat()})
            time.sleep(1)
            i += 1
            print("export data: \n", data, 100 * i // total_posts, end='\n' * 2)
            _set_task_progress(100 * i // total_posts)

        # send email with data to user
        send_email('[Microblog] Your blog posts',
                   sender=os.getenv("MAIL_DEFAULT_SENDER"), recipients=[user.email],
                   text_body=render_template('email/export_posts.txt', user=user),
                   html_body=render_template('email/export_posts.html', user=user),
                   attachments=[('posts.json', 'application/json;zh-CN',
                                 json.dumps({'posts': data}, ensure_ascii=False, indent=4))],
                   sync=True)
    except:
        _set_task_progress(100)
        app.logger.error('Unhandled exception', exc_info=sys.exc_info())
    # finally:
    #     # 设置进度条100%,将任务标记为已完成
    #     _set_task_progress(100)
