# -*- coding: utf-8 -*-
import sys,os
from imp import reload

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from flaskblog import models,create_app

reload(sys)
sys.setdefaultencoding('utf-8')


# Get the ENV from os_environ
env = os.environ.get('BLOG_ENV', 'dev')
# Create thr app instance via Factory Method
app = create_app('flaskblog.config.%sConfig' % env.capitalize())
# Init manager object via app object

# Init manager object via app object
manager = Manager(app)
migrate = Migrate(app, models.db)

# Create a new commands: server
# This command will be run the Flask development_env server
manager.add_command("server", Server())
manager.add_command("db", MigrateCommand)

@manager.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dict`
    """
    # 确保有导入 Flask app object，否则启动的 CLI 上下文中仍然没有 app 对象
    return dict(app=app,
                db=models.db,
                User=models.User,
                Post=models.Post,
                Comment=models.Comment,
                Tag=models.Tag,
                posts_tags=models.posts_tags,
                )

if __name__ == '__main__':
    manager.run()