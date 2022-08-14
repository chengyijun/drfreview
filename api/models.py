from django.db import models

# Create your models here.


class Classes(models.Model):
    classes_name = models.CharField(max_length=64, verbose_name="班级名称")

    def __str__(self) -> str:
        return f"{self.classes_name}"


class Student(models.Model):
    stu_name = models.CharField(max_length=64, verbose_name="学生姓名")
    classes = models.ForeignKey(to=Classes,
                                on_delete=models.CASCADE,
                                related_name='stus',
                                blank=True,
                                null=True,
                                verbose_name="所属班级")

    def __str__(self) -> str:
        return f"{self.stu_name} {self.classes}"