# encoding: utf-8
'''
03_lesson_template
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # 类
    class Person(object):
        name = 'SamMovedOn'
        age = 18

    # 创建类的实例
    p = Person()

    context = {
        'username': 'Sam',
        'gender': u'男',
        'age': 17,
        'person': p,  # 使用实例
        'websites': {
            'baidu': 'www.baidu.com',
            'google': 'www.google.com'
        }
    }
    return render_template('another/index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)

