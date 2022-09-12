# 从app包中导入 app这个实例
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


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


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user: {} , remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
