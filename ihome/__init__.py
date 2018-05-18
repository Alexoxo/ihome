# coding=utf-8
import redis
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import config_dic  # 导入配置类字典


d_base = SQLAlchemy()  # 创建SQLAlchemy对象


def create_app(config_name):
    """自定义工厂方法，返回一个应用，传入参数：配置类key名"""
    config_now = config_dic[config_name]  # 获取当前配置类

    # 创建Flask应用程序实例
    app = Flask(__name__)

    # 由类中导入配置
    app.config.from_object(config_now)

    d_base.init_app(app)  # d_base对象关联app

    # 创建rdis数据库链接对象
    redis_store = redis.StrictRedis(host=config_now.REDIS_HOST, port=config_now.REDIS_PORT)
    # 开启CSRF保护 只作保护校验，并不会生成csrf_token，需要另行完成
    CSRFProtect(app)
    # session信息存储
    Session(app)

    return app  # 返回flask应用实例