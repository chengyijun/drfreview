# Generated by Django 3.2.9 on 2022-08-14 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes_name', models.CharField(max_length=64, verbose_name='班级名称')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=64, verbose_name='学生姓名')),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classes', verbose_name='所属班级')),
            ],
        ),
    ]
