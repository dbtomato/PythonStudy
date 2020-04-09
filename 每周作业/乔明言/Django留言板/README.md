---
title: Djongo 留言板 项目笔记
tags: Djongo,Python,留言板
renderNumberedHeading: true
grammar_cjkRuby: true
---

Author:  Qiao My
Create_Time: 2020-3-31

[toc]

# 概览
## 项目目录结构
```bash
DjongoProject0 > tree
.
├── DjongoProject0
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── settings.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── wsgi.cpython-36.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app01                                       -- APP 文件夹
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── admin.cpython-36.pyc
│   │   ├── apps.cpython-36.pyc
│   │   ├── forms.cpython-36.pyc
│   │   ├── models.cpython-36.pyc
│   │   └── views.cpython-36.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations                              -- 迁移文件夹，存储用于迁移的Python文件，Djongo通过这些文件将models 同步到数据库
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-36.pyc
│   │       └── __init__.cpython-36.pyc
│   ├── models.py
│   ├── templates                               -- html 模板
│   │   └── index.html
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py                                   -- 所有命令行和Python 交互的入口
├── static                                      -- css、js 文件
│   ├── bootstrap-4.4.1-dist                    -- bootstrap框架
│   │   ├── css
│   │   │   ├── bootstrap-grid.css
│   │   │   ├── bootstrap-grid.css.map
│   │   │   ├── bootstrap-grid.min.css
│   │   │   ├── bootstrap-grid.min.css.map
│   │   │   ├── bootstrap-reboot.css
│   │   │   ├── bootstrap-reboot.css.map
│   │   │   ├── bootstrap-reboot.min.css
│   │   │   ├── bootstrap-reboot.min.css.map
│   │   │   ├── bootstrap.css
│   │   │   ├── bootstrap.css.map
│   │   │   ├── bootstrap.min.css
│   │   │   └── bootstrap.min.css.map
│   │   └── js
│   │       ├── bootstrap.bundle.js
│   │       ├── bootstrap.bundle.js.map
│   │       ├── bootstrap.bundle.min.js
│   │       ├── bootstrap.bundle.min.js.map
│   │       ├── bootstrap.js
│   │       ├── bootstrap.js.map
│   │       ├── bootstrap.min.js
│   │       └── bootstrap.min.js.map
│   └── jslib                                    -- jquery、popper 文件
│       ├── jquery-3.4.1.js
│       └── popper.js
└── templates
```
## Djongo 路由系统
![](./images/1585712800354.png)

## 请求流转路径
![](./images/1585741793851.png)

# 环境准备
## 安装MySQL
`brew install mysql`

## 安装 mysqlclient
`pip3 install mysqlclient`


安装报错
```
ld: library not found for -lssl
    clang: error: linker command failed with exit code 1 (use -v to see invocation)
    error: command 'gcc' failed with exit status 1
```

解决方法：
`env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib"  pip3 install mysqlclient`

## 创建 APP
Django规定，如果要使用模型，必须要创建一个app。
在pycharm中打开terminal，执行创建命令
`python manage.py start app01`

# 数据初始化
## 库表结构设计


## 配置数据库连接 - DjongoProject0/settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'message_board',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '192.168.11.101',
        'PORT': '23316',
    }
}
```

## 编写模型 app01/models.py
ORM (object relational mapping)
models.py 源码见附录
```python
# 基础模型，用来定义一些通用字段，比如创建时间和更新时间，通过被其他模型集成来使用
class CommonInfo(models.Model):

# 消息模型，既当前留言板项目中的留言消息模型，为迁移到数据库时实际对应的模型
class Message(CommonInfo):
```

## 激活模型  - DjongoProject0/settings.py
```python
INSTALLED_APPS = [
    ... ,
    'app01.apps.App01Config'
]
# 修改时区
TIME_ZONE = 'Asia/Shanghai'
```

## 生成迁移文件
不指定APP名称则初始化所有APP，任意修改均需迁移，这里的迁移指将models内定义的表和字段同步映射到数据库中
`python manage.py makemigrations app01`
```
(DjongoProject0) DjongoProject0 > python manage.py makemigrations app01
Migrations for 'app01':
  app01/migrations/0001_initial.py
    - Create model Message
```

## 迁移到数据库
`python manage.py migrate`
详细输出见  附录1

查看迁移SQL语句，0001表示app01内生成的迁移文件前缀
`python manage.py sqlmigrate app01 0001`

查看初始化的表、数据
app01_message 是自定义表，其他都是Djongo 自动生成的表
```
+------------+----------------------------+
| table_rows | table_name                 |
+------------+----------------------------+
|          0 | app01_message              |
|          0 | auth_group                 |
|          0 | auth_group_permissions     |
|         28 | auth_permission            |
|          0 | auth_user                  |
|          0 | auth_user_groups           |
|          0 | auth_user_user_permissions |
|          0 | django_admin_log           |
|          7 | django_content_type        |
|         18 | django_migrations          |
|          0 | django_session             |
+------------+----------------------------+
```

# admin 模块注册
## 修改 - app01/admin.py
添加如下代码
```python
from .models import Message
admin.site.register(Message)
```
> 注意：这里的注册仅仅是将模块注册进Djongo的admin管理后台，该注册对项目业务逻辑没有影响
## 创建 admin 模块管理员
`python manage.py createsuperuser`
```bash
(DjongoProject0) DjongoProject0 > python manage.py createsuperuser
Username (leave blank to use 'qiaomy'): admin
Email address: admin@outlook.com
Password: 
Password (again): 
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

## 通过 admin 管理后台操作数据
登录 http://127.0.0.1:8000/admin/ ，使用上一步中创建的用户和密码
![](./images/1585710153594.png)
![](./images/1585710250075.png)
![](./images/1585710287734.png)

查看添加的数据
```sql
root@localhost[message_board] 07:19:04>select * from app01_message;
+----+----------------------------+----------------------------+----------+---------+----------------------------+
| id | gmt_update                 | gmt_create                 | username | content | create_time                |
+----+----------------------------+----------------------------+----------+---------+----------------------------+
|  1 | 2020-03-31 11:35:56.627571 | 2020-03-31 11:35:37.263807 | 111      | 1111111 | 2020-03-31 11:35:37.263827 |
+----+----------------------------+----------------------------+----------+---------+----------------------------+
1 row in set (0.00 sec)
```

# 前端

## 前端依赖环境准备
**下载，如需解压则解压**
https://github.com/twbs/bootstrap/releases/download/v4.4.1/bootstrap-4.4.1-dist.zip
https://code.jquery.com/jquery-3.4.1.js
https://unpkg.com/@popperjs/core@2/dist/umd/popper.js

**拷贝到项目**
在项目根目录创建 static 文件夹，将 bootstrap 文件夹放入 static文件夹

创建 static/jslib 文件夹，将 jQuery、Popper 文件放入文件夹

**修改配置，导入静态样式文件**
修改 **DjongoProject0/DjongoProject0/setting.py**，添加如下配置，否则页面将无法加载样式
```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```

## 编写HTML 模板文件
见 附录3

# 后端
## 编写视图 - app01/views.py
此处实现与前端的直接交互：
- 前端通过 DjongoProject0/DjongoProject0/urls.py 路由配置接找到对应的views方法
- views 方法可以通过render方法向指定 HTML文件返回数据，HTML文件中的Djongo模板语言获取数据并展示
见 附录2

## 修改路由 - DjongoProject0/urls.py
添加如下代码
```python
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index')
]
```

## 编写表单 - app01/forms.py
Djongo 可以将表单视作一个model，但可能无法正确匹配，forms.py作为一个中间层，将前端表单转换为一个正确的model
```python
from django import forms

from .models import Message

class MessageForm(forms.ModelForm):
    # 元信息
    class Meta:
        model = Message
        fields = ['username', 'content']
        # createtime 时间不需要用户填写，所以此处只有两个字段
```

# 参考资料
[python mac下安装 MySQLdb模块的坑 library not found for -lssl]https://www.jianshu.com/p/86367222dd74

# 附录
## 输出
### 附录1
```bash
(DjongoProject0) DjongoProject0 > python manage.py migrate
System check identified some issues:

WARNINGS:
?: (mysql.W002) MySQL Strict Mode is not set for database connection 'default'
        HINT: MySQL's Strict Mode fixes many data integrity problems in MySQL, such as data truncation upon insertion, by escalating warnings into errors. It is strongly recommended you activate it. See: https://docs.djangoproject.com/en/3.0/ref/databases/#mysql-sql-mode
Operations to perform:
  Apply all migrations: admin, app01, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying app01.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
```

## 源码
### 附录2 - views.py
```python
from django.shortcuts import render, redirect, reverse
from django.http.response import HttpResponse
from django.contrib import messages as django_messages

from .forms import MessageForm
from .models import Message

# Create your views here.
def index(request):
    # return HttpResponse("Hello World")

    message_form = MessageForm()
    # 判断是否 POST 请求，是的话发送数据
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        # 检查表单是否合法
        if message_form.is_valid():
            # 如果合法，则保存数据
            message_form.save()
            # 调用 django.contrib.messages 的方法，返回留言状态
            # django.contrib.messages 模块自动生成一个`messages`变量，禁止在 context中定义同名变量，会覆盖当前默认变量
            django_messages.success(request, '留言成功')
            return redirect(reverse('index'))

    # 拿到所有留言
    messages = Message.objects.all()
    # 留言赋值给 message_list
    context = {
        # 'title': '乔明言',
        'message_list': messages,
        'form': message_form
    }
    # rander()渲染，将context渲染到 index.html
    return render(request, 'index.html', context)
```

### 附录3 - index.html

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>公开课：实战Django的留言版设计到部署</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="{% static '/bootstrap-4.4.1-dist/css/bootstrap.min.css' %}" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

</head>
<body>

<nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
  <a class="navbar-brand" href="#">知数堂</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarsExampleDefault">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">留言板 <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://ke.qq.com/course/1650906?tuin=34432a0f" target="_blank">知数堂公开课：实战Django的留言版设计到部署 本周四晚上8点30分</a>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="text" placeholder="Python课程" aria-label="Search">
      <button class="btn btn-secondary my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>

<main role="main" class="container" style="padding-top: 80px;">
    <!-- 返回留言结果。对应views.py中 django.contrib.messages 模块自动生成的`messages`变量 -->
    {% if messages %}
        {% for message in messages %}
        <div class="alert alert-primary" role="alert">
          {{ message }}
        </div>
        {% endfor %}
    {% endif %}
        <!-- 表单，提交到 views.py -->
        <!-- 根据action="{% url 'index' %}" 中的`index`，在urls.py中找到 path('index/', views.index, name='index') 中配置的`views.index`-->
        <form method="post" action="{% url 'index' %}">
            <!-- 调用Djongo form方法必须写 csrf_token-->
            {% csrf_token %}
            <div class="form-group">
                <label for="nickname_input">昵称</label>
                <input type="text" maxlength="64" name="username" class="form-control" id="nickname_input" placeholder="用户名">
            </div>

            <div class="form-group">
                <label for="comment_input">留言</label>
                <textarea class="form-control" name="content" id="comment_input" rows="3" maxlength="65535" placeholder="请文明留言"></textarea>
            </div>
            <div class="form-group">
                <button type="submit" class="btn btn-primary">提交</button>
            </div>
        </form>

        {% if message_list %}
            <!-- 展示留言：循环 message_list，生成表单，message_list对应views.py中的message_list -->
            {% for message in message_list %}
                <div class="card" style="margin-top: 10px;">
                    <div class="card-body">
                        <h5 class="card-title">
                            {{message.username}}
                            <span class="text-muted" style="font-size: 0.9rem">
                                {{message.create_time | date:'Y-m-d H:i:s'}}
                            </span>
                        </h5>
                        <p class="card-text">留言：{{ message.content|safe }}</p>
                    </div>
                </div>
            {% endfor %}
        <!-- 没有留言时默认展示 -->
        {% else %}
            <p>还没有人发表留言。</p>
        {% endif %}
</main><!-- /.container -->

<footer class="text-center" style="margin-top: 10px">
<a href="http://www.beian.miit.gov.cn/" target="_blank">备案号：浙ICP备14008409号-2</a>
</footer>

<script src="{% static '/jslib/jquery.min.js' %}"></script>
<script src="{% static '/jslib/popper.js' %}"></script>
<script src="{% static '/bootstrap-4.4.1-dist/js/bootstrap.min.js' %}"></script>

</body>
</html>
```
