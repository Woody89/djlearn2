# djlearn2
A project for testing django and smthing else technoligies

1.测试django

2.涵盖知识点:

  	……Celery-异步任务神器
  
  	……Session-显示当前登录用户、记录评论用户信息
  
  	……
  
3.测试git页面功能

You should install redis first!!! 
1.when use celery, should execute commands bellow in 2 cmds:
	1.python manage.py runserver 127.0.0.1:9000
	2.celery -A blog worker -l info
