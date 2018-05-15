# coding=utf-8
from flask import Flask

# 创建Flask应用程序实例
biu = Flask(__name__)


@biu.route('/')
def index():
    return 'hey here is my index'


if __name__ == '__main__':
    # 运行开发web服务器
    biu.run(debug=True)
