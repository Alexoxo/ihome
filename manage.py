# coding=utf-8
from flask import Flask


class Config(object):
    """配置类"""
    DEBUG = True



# 创建Flask应用程序实例
biu = Flask(__name__)

biu.config.from_object(Config)


@biu.route('/')
def index():
    return 'hey here is my index'


if __name__ == '__main__':
    # 运行开发web服务器
    biu.run()
