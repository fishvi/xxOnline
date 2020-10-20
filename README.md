# xxOnline在线学习网
[![Python](https://img.shields.io/badge/Python-3.7.3-blue)](https://www.python.org/downloads/release/python-373/)
[![Django](https://img.shields.io/badge/Django-2.2-blue)](https://docs.djangoproject.com/en/2.2/releases/)
[![xadmin](https://img.shields.io/badge/xadmin-0.6.0-blue)](https://github.com/sshwsfc/xadmin)
[![MySQL](https://img.shields.io/badge/MySQL-5.7-blue)](https://dev.mysql.com/downloads/mysql/)
[![redus](https://img.shields.io/badge/redis-3.0.503-blue)](https://github.com/ServiceStack/redis-windows/tree/master/downloads)


**基于Django2.2和xadmin的在线教育学习平台**

## 安装依赖  
```python
pip install -r requirements.txt
```

### MySQL：
>1. 下载[MySQL 5.7](https://dev.mysql.com/downloads/mysql/)（最新版MySQL可能会出现某些问题）
>2. 新建数据库
>3. 在settings.py中配置MySQL  
>```python
>   DATABASES = {
>       'default': {
>           'ENGINE': 'django.db.backends.mysql',
>           'NAME': '数据库名称',
>           'USER': '用户名',
>           'PASSWORD': '密码',
>           'HOST': '127.0.0.1'
>       }
>   }
>```
>4. 安装mysqlclient
>```python
>    pip install mysqlclient
>```  
>&emsp;&emsp;**注意：** 如果是Windows，也许直接安装mysqlclient会出错，请前往[这里](https://www.lfd.uci.edu/~gohlke/pythonlibs/)找到mysqlclient下载，再pip install下载的文件。  

### redis：
##### &emsp;如果Linux：  
        $ sudo apt-get install redis-server
        $ sudo apt-get install redis-cli
##### &emsp;如果Windows:
>&emsp;&nbsp;&nbsp;请前往[这里](https://github.com/ServiceStack/redis-windows/tree/master/downloads)下载安装  

&emsp;关于redis在本项目中的用处请往下翻至底。

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

>> Superuser created successfully.
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
### ✨*写在最后：*
1. 关于**手机验证码：**  
&emsp;在本项目中的手机验证码是通过一个[随机函数](https://github.com/fishvi/xxOnline/blob/master/apps/utils/random_str.py)生成了四位随机数，然后存入redis，并设定了一个有效时间60s。然后使用第三方短信平台发送生成的随机数至用户手机中，我这里用的是[云片网](https://www.yunpian.com/product/domestic-sms)。  
&emsp;但是云片网的签名实在是难以申请......如果你也同样暂时申请不下来，别慌，我已经写好了用于[测试的代码](https://github.com/fishvi/xxOnline/blob/master/apps/utils/YunPian.py)，启动redis后(redis-server)，再用get命令(redis-cli)，即可得到刚刚生成的验证码。  
&emsp;如果你申请到了签名或是有了其他替代方案，请自行修改[settings.py](https://github.com/fishvi/xxOnline/blob/master/xxOnline/settings.py)和[YunPian.py](https://github.com/fishvi/xxOnline/blob/master/apps/utils/YunPian.py)中的相关内容。  

2. 关于**课程视频：**  
&emsp;可以用到阿里云的对象存储OSS进行管理。

2. 关于**部署：**  
&emsp;个人使用的uwsgi和nginx。