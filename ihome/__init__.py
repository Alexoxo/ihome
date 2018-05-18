# coding=utf-8
import redis
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import Config




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