# 从app包中导入 app这个实例
from app import app
from flask import render_template


# 2个路由
@app.route('/')
@app.route('/index')
# 1个视图函数
def index():
    user = {'username': 'San Francisco'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
