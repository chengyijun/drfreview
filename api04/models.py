from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=64, verbose_name="课程名称")
    # 不生成数据库字段  反向关联 course_obj.prices.all() 拿到所有的价格策略
    prices = GenericRelation("PricePolicy")


class DegreeCourse(models.Model):
    name = models.CharField(max_length=64, verbose_name="课程名称")
    # 不生成数据库字段  反向关联
    prices = GenericRelation("PricePolicy")


class PricePolicy(models.Model):
    price = models.FloatField(verbose_name="价格")

    content_type = models.ForeignKey(ContentType, verbose_name="关联表的表名", on_delete=models.CASCADE)
    object_id = models.IntegerField(verbose_name="关联表中的行ID")
    # 不生成字段 辅助content type 操作
    # PricePolicy.objects.create(price=9.9, content_object=course_obj)
    content_object = GenericForeignKey("content_type", "object_id")
