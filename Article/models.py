from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    body = RichTextField(verbose_name='مطلب')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی')
    image = models.ImageField(null=True, blank=True, upload_to='Article/images', verbose_name='تصویر')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    slug = models.SlugField(null=True, blank=True, unique=True)

    def get_absolute_url(self):
        return reverse("Articles:article_detail", args=[self.slug])

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Article, self).save()

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return f"{self.title} - {self.author} - {self.created_time} - {self.category}"
