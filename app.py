# encoding: utf-8
'''
04_control_statements_and_filter
if 条件判断语句
for 循环控制语句
filter 过滤器
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    user = {
        "name": 'Sam',
        "age": 25
    }
    books = [
        {
            'name': u'西游记',
            'author': u'吴承恩',
            'price': 109
        },
        {
            'name': u'红楼梦',
            'author': u'曹雪芹',
            'price': 200
        },
        {
            'name': u'三国演义',
            'author': u'罗贯中',
            'price': 120
        },
        {
            'name': u'水浒传',
            'author': u'施耐庵',
            'price': 130
        }
    ]

    fruit = ['apple', 'banana', 'orange']

    return render_template('another/index.html', user=user, books=books, fruit=fruit)


if __name__ == '__main__':
    app.run(debug=True)
