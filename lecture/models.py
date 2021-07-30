from django.db import models


class Lecture(models.Model):
    class_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    detail_subject = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    price = models.CharField(max_length=20)
    lecture_image = models.ImageField(upload_to='lecture/images/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.class_name

    def get_absolute_url(self):
        return f'/lecture/{self.pk}/'
