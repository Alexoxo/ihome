# coding=utf-8
import redis
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session


class Config(object):
    """配置类"""
    DEBUG = True
    # 设置SECRET_KEY
    SECRET_KEY = "J90hCOvP1R1tdl5nRpB2ftpikq9Zbd/WpmrX9299ig4nPDwPeJXRlcQHV6LzA7j1"
    # mysql相关配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@127.0.0.1:3306/ihome_db'  # 设置数据库链接地址
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 关闭追踪数据库的修改
    # redis相关配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    # session存储到哪个数据库中,并指定数据库信息
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True  # 开启session签名加密
    PERMANENT_SESSION_LIFETIME = 86400 * 2  # 设置session过期时间(秒) 默认31天


# 创建Flask应用程序实例
biu = Flask(__name__)

# 由类中导入配置
biu.config.from_object(Config)

# 创建sqlAlchemy对象
d_base = SQLAlchemy(biu)
# 创建rdis数据库链接对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启CSRF保护 只作保护校验，并不会生成csrf_token，需要另行完成
CSRFProtect(biu)
# session信息存储
Session(biu)


@biu.route('/')
def index():
    session["ali"] = "boom"
    return 'hey here is my index'


if __name__ == '__main__':
    # 运行开发web服务器
    biu.run()
