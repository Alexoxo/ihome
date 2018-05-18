# coding=utf-8
from flask_script import Manager  # 通过脚本的方式runserver来启动项目
from flask_migrate import Migrate, MigrateCommand  # 通过迁移模型类的方式管理数据库表
from ihome import create_app, d_base

# 创建biu应用
biu = create_app("development")

# 创建Manager管理对象
manager = Manager(biu)  # 可以通过python manage.py runserver启动项目
Migrate(biu, d_base)
manager.add_command("m_db", MigrateCommand)  # 参数：name, command 添加迁移命令


@biu.route('/', methods=["GET", "POST"])
def index():

    return 'hey here is my index'


if __name__ == '__main__':
    # 运行开发web服务器
    manager.run()
    # biu.run()