# encoding: utf-8
'''
26_blog_rq_queue
blog项目添加rq消息队列
'''
from app import create_app, db
from app.models import User, Post, Notification, Message, Task

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            "Notification": Notification, 'Task': Task}


if __name__ == '__main__':
    app.run(debug=True)
