# encoding: utf-8
'''
25_blog_user_notifications
给用户发送私信后，在Message栏显示未读消息徽章
'''
from app import create_app, db
from app.models import User, Post, Notification, Message

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            "Notification": Notification}


if __name__ == '__main__':
    app.run(debug=True)
