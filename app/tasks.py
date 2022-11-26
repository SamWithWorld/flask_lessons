# !/usr/local/bin python3
# coding: utf-8
# @FileName  :tasks.py
# @Time      :2022/11/26 07:51
# @Author    :Sam

import time
from rq import get_current_job


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

# from redis import Redis
# import rq
# queue = rq.Queue('microblog-tasks', connection=Redis.from_url('redis://'))
# job = queue.enqueue('app.tasks.example', 23)
