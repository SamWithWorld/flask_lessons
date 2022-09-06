# encoding: utf-8
'''
05_template_inherit_url_for

模板继承

集成 Bootstrap

url_for 反转url

加载静态文件

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
