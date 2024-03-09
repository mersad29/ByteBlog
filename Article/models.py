from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from Account.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    created_time = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='تاریخ انتشار')
    color = models.CharField(max_length=50, blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name='وضعیت انتشار')


    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    body = RichTextField(verbose_name='مطلب')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='نویسنده')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی')
    image = models.ImageField(null=True, blank=True, upload_to='Article/images', verbose_name='تصویر')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    slug = models.SlugField(null=True, blank=True, unique=True, verbose_name='لینک مقاله')
    published = models.BooleanField(default=False, verbose_name='وضعیت انتشار')
    color = models.CharField(max_length=20, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("Articles:article_detail", args=[self.slug])

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        # self.slug = slugify(self.title)
        super(Article, self).save()

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return f"{self.title} - {self.author} - {self.created_time}"


class Like(models.Model):
    article = models.ForeignKey(Article, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'

    def __str__(self):
        return self.created_at


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='مقاله')
    name = models.CharField(max_length=100, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    body = models.TextField(verbose_name='متن نظر')
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='replies',
                               verbose_name='نظر والد')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    published = models.BooleanField(default=False, verbose_name='وضعیت انتشار')


    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return f"{self.name} - {self.email} - {self.article.title}"
