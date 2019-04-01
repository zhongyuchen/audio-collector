# audio-collector

Audio collecting website for building a dataset for Digital Signal Processing course project

## Todo

* 随机出下一个词
* 有按钮可以截词
* 记录到一半，人走了，回来之后还能继续（存一个小文件，再读回去）
* 导出无后台版
* wav的编码方式必须是非压缩的
* 显示round和词编号
* 强制输入学号，初始为空
* 按钮加上tip

## Command Lines

* start django project and app
```commandline
django-admin startproject audio_collector
python manage.py startapp collector
```

* Let Django builds basic tables in MySQL
```commandline
python manage.py migrate
```

* Django models -> MySQL tables
```commandline
python manage.py makemigrations collector
python manage.py migrate
```

* MySQL tables -> Django models
```commandline
python manage.py inspectdb > collector/models.py
```

* create superuser
```commandline
python manage.py createsuperuser
```

* run server
```commandline
python manage.py runserver
```

## Login Info

| Role      | Username  | Password  |
| --------- | --------- | --------- |
| superuser | admin     | superuser |
| user      | student   | person000 |
