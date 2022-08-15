from django.db import models


# Create your models here.

class UserInfo(models.Model):
    user_name = models.CharField(max_length=64, verbose_name="用户名")


class Role(models.Model):
    role_name = models.CharField(max_length=64, verbose_name="角色名")
    users = models.ManyToManyField(to=UserInfo, related_name="roles")
