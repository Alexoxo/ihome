# coding=utf-8
import redis
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager  # 通过脚本的方式runserver来启动项目
from flask_migrate import Migrate, MigrateCommand  # 通过迁移模型类的方式管理数据库表
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

# 创建Manager管理对象
manager = Manager(biu)  # 可以通过python manage.py runserver启动项目
Migrate(biu, d_base)
manager.add_command("m_db", MigrateCommand)  # 参数：name, command 添加迁移命令


@biu.route('/')
def index():
    session["ali"] = "boom"
    return 'hey here is my index'


if __name__ == '__main__':
    # 运行开发web服务器
    manager.run()
