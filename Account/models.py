from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    f_name = models.CharField(max_length=100, verbose_name='نام')
    l_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    phone = models.CharField(max_length=14, unique=True, verbose_name='شماره تلفن')
    linkedin = models.CharField(max_length=250, verbose_name='آدرس لینکدین')
    telegram = models.CharField(max_length=250, verbose_name='تلگرام')
    github = models.CharField(max_length=250, verbose_name='آدرس گیتهاب')
    image = models.ImageField(upload_to='Account/images', null=True, blank=True, verbose_name='تصویر پروفایل')