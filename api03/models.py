from django.db import models


# Create your models here.
class MyBaseModelManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False)


class MyModelManager(MyBaseModelManager):
    def get_id_gt_5(self):
        return self.model.mm.filter(id__gt=5)

    def get_id_lt_5(self):
        return self.model.mm.filter(id__lt=5)


class Dog(models.Model):
    name = models.CharField(max_length=64, verbose_name="名字")
    is_delete = models.BooleanField(default=False, verbose_name="是否被删除")

    mm = MyModelManager()

    def __str__(self):
        return f"{self.name} - {self.is_delete}"
