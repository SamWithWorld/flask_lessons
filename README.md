26_blog_rq_queue



    blog项目添加rq消息队列，将发送邮件任务交给rq处理
    
    -2.使用redis-server命令启动redis
    
    -1.在项目目录下执行rq worker microblog-tasks命令启动worker
    
    0. 发送邮件，在tasks.py中export_posts调用send_mail发送邮件，通过sync字段控制异步发送还是同步发送邮件
    
    1. 搭建Elasticsearch，启动 Elasticsearch
    
    2. 搭建Kibana，启动 Kibana
    
    3. 新建microblog.env后配置以下选项：
    
        MAIL_SERVER='smtp.163.com'
        MAIL_PORT=25
        MAIL_USE_TLS=False
        MAIL_USERNAME='<你的163邮箱地址>'
        MAIL_PASSWORD='<你的163邮箱密码>'
        MAIL_DEFAULT_SENDER='<你的163邮箱地址>'
        BD_TRANSLATOR_APPID='<你的百度翻译APPID>'
        BD_TRANSLATOR_KEY='<你的百度翻译密钥>'
        ELASTICSEARCH_URL='<Elasticsearch 地址>'
        
    4. 安装gunicorn、nginx、supervisor,配置/usr/local/etc/supervisord.ini文件，添加要监听的子进程，启动：supervisord -c /usr/local/etc/supervisord.ini
    
    监听gunicorn、nginx子进程如下：
    
    [program:gunicorn]
    command=/Library/Frameworks/Python.framework/Versions/3.7/bin/gunicorn -w 2 -b 127.0.0.1:5000 microblog:app
    directory=/Users/sam/PycharmProjects/flask_lessons
    autostart=true
    autorestart=true
    user=sam
    redirect_stderr=true
    
    [program:nginx]
    command=/usr/local/bin/nginx -g 'daemon on;'
    autostart=true
    autorestart=true
    user=sam
    redirect_stderr=true
