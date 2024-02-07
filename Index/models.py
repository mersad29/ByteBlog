from django.db import models
from ckeditor.fields import RichTextField


class HeaderBasement(models.Model):
    title = RichTextField(blank=True, null=True, verbose_name='عنوان')
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'عنوان بالای صفحه'
        verbose_name_plural = 'عنوان بالای صفحه'

    def __str__(self):
        return self.title


class FooterBasement(models.Model):
    description = RichTextField(blank=True, null=True, verbose_name='توضیحات پایین صفحه')
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'فوتر'
        verbose_name_plural = 'فوتر'

    def __str__(self):
        return self.description


class Inbox(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    body = models.TextField(verbose_name='متن نظر')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")

    class Meta:
        verbose_name = 'صندوق پیام'
        verbose_name_plural = 'صندوق پیام ها'

    def __str__(self):
        return f"{self.name} - {self.email} - {self.created_at}"
