from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class MyUser(AbstractUser):
    """自定义用户模型类"""

    # 额外增加 mobile 字段      长度11位        号码唯一        别名
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')

    # 对当前表进行相关设置:
    # class Meta:
    #     db_table = 'tb_users'

    # 在 str 魔法方法中, 返回用户名称
    def __str__(self):
        return self.username
