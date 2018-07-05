##下载代码
    git cone 

##安装依赖
    pip install -r requirements.txt
        
##修改配置
    vim config.py
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:kbsonlong@blog_db:8080/blog'


##初始化数据库
    python manage.py db init
    python manage.py db migrate -m "Init DB"
    python manage.py db upgrade
    
##修改主机监听端口

    vim manage.py
    manager.add_command("server", Server(host='0.0.0.0', port=5000))
    
##启动服务
    python manage.py server