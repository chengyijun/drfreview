from django.db import models


# Create your models here.

class Role(models.Model):
    role_name = models.CharField(max_length=64, verbose_name="角色名称")
    # 多对多 不需要 on_delete
    # 多对多 由于会产生中间表 中间表产生关联两头的外键 所以不会在本表中生成一个新的外键字段
    users = models.ManyToManyField(to="UserInfo", related_name="user_roles", null=True, blank=True)


class Group(models.Model):
    group_name = models.CharField(max_length=64, verbose_name="组名称")


class UserInfo(models.Model):
    username = models.CharField(max_length=64, verbose_name="用户名")
    # ForeignKey 会在本表产生一个 group_id 的外键字段
    # related_name="group_users" 反向查询   其实就相当于在 Group表中 产生一个虚拟的 group_users字段 用户查询 group_obj.group_users.all()
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE, related_name="group_users", null=True, blank=True)


class UserToken(models.Model):
    token = models.CharField(max_length=64, verbose_name="token")
    user = models.OneToOneField(to=UserInfo, on_delete=models.CASCADE, related_name="user_token", null=True, blank=True)
    # OneToOneField 相当于 ForeignKey + unique约束
    # user = models.ForeignKey(to=UserInfo, on_delete=models.CASCADE, related_name="user_token", null=True, blank=True,
    #                          unique=True)
