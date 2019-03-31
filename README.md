# audio-collector

Audio collecting website for building a dataset for Digital Signal Processing course project

## Todo

* 随机出下一个词
* 有按钮可以截词
* 记录到一半，人走了，回来之后还能继续（存一个小文件，再读回去）

```commandline
django-admin startproject audio_collector
python manage.py startapp collector
```

Let Django builds basic tables in MySQL
```commandline
python manage.py migrate
```

Django models -> MySQL tables
```commandline
python manage.py makemigrations collector
python manage.py migrate
```

MySQL tables -> Django models
```commandline
python manage.py inspectdb > collector/models.py
```

```commandline
python manage.py createsuperuser
```

```commandline
python manage.py runserver
```
