from django.db import models
from common.models import CustomUser as User


class Category(models.Model):
    class_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.class_name

    def get_absolute_url(self):
        return '/lecture/category/{0}'.format(self.slug)

    class Meta:
        verbose_name_plural = 'Categories'


class Lecture(models.Model):
    class_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    detail_subject = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    price = models.CharField(max_length=20)
    lecture_image = models.ImageField(upload_to='lecture/images/%Y/%m/%d/', blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    member = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='member')
    max_member = models.IntegerField(default=10)


    def __str__(self):
        return self.class_name

    def get_absolute_url(self):
        return f'/lecture/{self.pk}/'
