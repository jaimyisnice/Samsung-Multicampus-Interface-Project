from django.db import models


class Lecture(models.Model):
    class_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    detail_subject = models.CharField(max_length=50)
    date = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.class_name
