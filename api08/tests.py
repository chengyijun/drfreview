import os
import sys

import django

sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drfreview.settings")

django.setup()
# from django.contrib.auth.models import User
# from api08.models import MyUser
from django.contrib import auth

# users = MyUser.objects.all()
# print(users)
#
# MyUser.objects.create_superuser(username="tank", email="tank@qq.com", password="tank", mobile="13345788956")

# 查询要登录的用户是否存在 如果存在返回该用户对象
login_user = auth.authenticate(username="abel", password="abel")
print(login_user)
# 通过login()方法 将用户对象 绑定到request对象上  完成登录
# auth.login(request=request,user=login_user)

"""
[补充]Django的用户莫模型基类提供的方法
User.set_password() 设置密码
User.check_password() 校验明文密码
User.objects.create() 新建User对象，但是密码不会加密
User.objects.create_user() 新建User对象，并且自动加密密码
User.objects.create_superuser() 新建User对象，并且自动加密密码，并且是一个管理员is_staff=True
make_password(xxx)也可以将密码xxx设置为秘文
"""
