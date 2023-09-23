from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.
class Product(models.Model): 
    owner = models.ForeignKey(User, on_delete = models.CASCADE)


class Lesson(models.Model):
    name = models.CharField(max_length = 200)
    URL = models.URLField()
    length = models.SmallIntegerField()
    inProduct = models.ManyToManyField(Product)


class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE)
    viewedAt = models.DateTimeField(auto_now_add = True)
    viewed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.viewedAt and self.lesson.length:
            currentTime = datetime.datetime.now()
            differenceInMinutes = int((currentTime - self.viewedAt).total_seconds() / 60)