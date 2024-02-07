from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField

class CustomUser(AbstractUser):
    f_name = models.CharField(max_length=100, verbose_name='نام')
    l_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    phone = models.CharField(max_length=14, unique=True, verbose_name='شماره تلفن')
    linkedin = models.CharField(max_length=250, verbose_name='آدرس لینکدین')
    telegram = models.CharField(max_length=250, verbose_name='تلگرام')
    instagram = models.CharField(max_length=250, verbose_name='اینستاگرام')
    github = models.CharField(max_length=250, verbose_name='آدرس گیتهاب')
    about_me = RichTextField(verbose_name='درباه من(نمایش در بخش درباه من)')
    image = models.ImageField(upload_to='Account/images', null=True, blank=True, verbose_name='تصویر پروفایل')