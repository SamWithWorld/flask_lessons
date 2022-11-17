# encoding: utf-8
'''
24_project_js_magic
当鼠标悬停在用户名上，就会弹出窗口，在弹窗中显示用户的简要信息
'''
from app import create_app, db
from app.models import User, Post

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':
    app.run(debug=True)
