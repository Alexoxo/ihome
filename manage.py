# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Config(object):
    """配置类"""
    DEBUG = True
    # mysql相关配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@127.0.0.1:3306/ihome_db'  # 设置数据库链接地址
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 关闭追踪数据库的修改



# 创建Flask应用程序实例
biu = Flask(__name__)

# 由类中导入配置
biu.config.from_object(Config)

# 创建sqlAlchemy对象
d_base = SQLAlchemy(biu)



@biu.route('/')
def index():
    return 'hey here is my index'


if __name__ == '__main__':
    # 运行开发web服务器
    biu.run()
