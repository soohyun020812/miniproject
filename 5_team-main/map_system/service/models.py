from django.db import models

class MyModel(models.Model):
    store_name = models.CharField(max_length=1000)
    store_code = models.CharField(max_length=1000)
    store_segment = models.CharField(max_length=1000)
    address_dong = models.CharField(max_length=1000)
    address_road = models.CharField(max_length=1000)
    longitude = models.FloatField()
    latitude = models.FloatField()



class UserInputModel(models.Model):
    # 점포위치
    store_location = models.CharField(max_length=1000)
    # 업종선택
    store_select = models.CharField(max_length=1000)
    # 분석영역
    store_area = models.IntegerField(max_length=1000)

from django.db import models

class MyModel(models.Model):
    store_name = models.CharField(max_length=1000)
    store_code = models.CharField(max_length=1000)
    store_segment = models.CharField(max_length=1000)
    address_dong = models.CharField(max_length=1000)
    address_road = models.CharField(max_length=1000)
    longitude = models.FloatField()
    latitude = models.FloatField()



class Signup(models.Model):
    nickname = models.CharField(max_length=1000)
    userid = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    passwordcheck = models.CharField(max_length=1000)
    email = models.EmailField()
    phone = models.CharField(max_length=1000)


