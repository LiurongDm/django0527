from django.db import models
# Create your models here.
from tinymce.models import HTMLField


class User(models.Model):
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=240)
    tel = models.CharField(max_length=20)
    headimg = models.CharField(max_length=200,default=1)




class Goods(models.Model):
    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=255)
    price = models.IntegerField()
    detail = models.CharField(max_length=255)

    class Meta:
        db_table = 'goods'
    #
    #
    # def __str__(self):
    #     return self.name


# 下面这两个表是用于测试 后台管理的级联关系
class Grade(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    sex = models.CharField(max_length=50)

    s_grade = models.ForeignKey(Grade,on_delete='on_delete')

class News(models.Model):
    title = models.CharField(max_length=250)
    content = HTMLField()



