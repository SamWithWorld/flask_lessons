# encoding: utf-8
'''
04_control_statements_and_filter
if 条件判断语句
for 循环控制语句
filter 过滤器
'''
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('another/index.html')


@app.route('/user/<name>')
def user(name):
    # 输出视图函数index的url
    print(url_for('index', _external=True, page=2, version=1))
    return render_template('user.html', name=name)


if __name__ == '__main__':
    bootstrap = Bootstrap(app)
    app.run(debug=True)
