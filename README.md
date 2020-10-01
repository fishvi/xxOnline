# xxOnline在线学习网
[![Python](https://img.shields.io/badge/Python-3.7.3-blue)](https://www.python.org/downloads/release/python-373/)
[![Django](https://img.shields.io/badge/Django-2.2-blue)](https://docs.djangoproject.com/en/2.2/releases/)
[![xadmin](https://img.shields.io/badge/xadmin-0.6.0-blue)](https://github.com/sshwsfc/xadmin)
[![MySQL](https://img.shields.io/badge/MySQL-5.7-blue)](https://dev.mysql.com/downloads/mysql/)
[![redus](https://img.shields.io/badge/redis-3.0.503-blue)](https://github.com/ServiceStack/redis-windows/tree/master/downloads)


基于Django2.2和xadmin的在线教育学习平台

## 安装依赖  
```python
pip install -r requirements.txt
```

### MySQL：
>1. 下载[MySQL](https://dev.mysql.com/downloads/mysql/)
>2. 新建数据库
>3. 在settings.py中配置MySQL  
>```python
>DATABASES = {
>    'default': {
>        'ENGINE': 'django.db.backends.mysql',
>        'NAME': '数据库名称',
>        'USER': '用户名',
>        'PASSWORD': '密码',
>        'HOST': '127.0.0.1'
>    }
>}
>```
>**注意：** 如果你是Windows，也许在安装mysqlclient时会出错，请前往[这里](https://www.lfd.uci.edu/~gohlke/pythonlibs/)找到mysqlclient下载后直接pip install。

### redis：
#### 如果Linux：  
    $ sudo apt-get install redis-server
    $ sudo apt-get install redis-cli
#### 如果Windows:
>请前往[这里](https://github.com/ServiceStack/redis-windows/tree/master/downloads)下载安装

&nbsp;  
&nbsp;  
## 运行项目  
应用数据模型，创建数据库表:
```python
python manage.py makemigrations

python manage.py migrate
```

启动项目：
```python
python manage.py runserver
```

浏览器访问：http://localhost:8000/ 或者 http://127.0.0.1:8000/

&nbsp;  
&nbsp;  
## 后台管理  
创建一个管理员账号：  
```python
python manage.py createsuperuser

Username: admin  # 键入你想要使用的用户名，然后按下回车键

Email address: admin@example.com  # 然后提示你输入想要使用的邮件地址

Password: **********  # 输入密码
Password (again): *********

Superuser created successfully.
```

启动项目：
```python
python manage.py runserver
```

浏览器访问：http://localhost:8000/xadmin 或者 http://127.0.0.1:8000/xadmin

&nbsp;  
&nbsp;  
&nbsp; 
***
### ✨*写在最后的碎碎念：*
1. 关于通过**手机验证码**的登录/注册，我这里用的是云片网，但是云片网的签名实在是难以申请...为了测试，我就直接在redis中用get得到验证码了。如果你申请到了签名或是有了其他替代方案，请自行修改[settings.py](https://github.com/fishvi/xxOnline/blob/master/xxOnline/settings.py)和[YunPian.py](https://github.com/fishvi/xxOnline/blob/master/apps/utils/YunPian.py)中的内容。  

2. 关于**课程视频**，可以用到阿里云的对象存储OSS进行管理。

3. 有些**细节**问题，如后台上传的图片在前端页面显示不全以及缩放不协调等问题，待我再看看。

4. 关于**部署**，后面再更新...

5. **任重而道远。**