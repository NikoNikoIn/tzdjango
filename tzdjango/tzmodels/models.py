from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.utils import timezone

 
class Product(models.Model): 
    name = models.CharField(max_length = 200, default="Product")
    owner = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length = 200)
    URL = models.URLField()
    length = models.SmallIntegerField()
    inProduct = models.ManyToManyField(Product)

    def __str__(self):
        return self.name


class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE)
    viewedTime = models.IntegerField(default = 0)
    viewed = models.BooleanField(default = False)
    lastView = models.DateTimeField(default = timezone.now())

    def save(self, *args, **kwargs):
        if self.viewedTime and self.lesson.length:
            if self.viewedTime / self.lesson.length >= 0.8 and self.viewedTime != 0:
                self.viewed = True
            else:
                self.viewed = False
        self.lastView = timezone.now()
        super().save(*args, **kwargs)

    def clean(self):
        if self.viewedTime > self.lesson.length:
            raise ValidationError("Viewed time cannot be greater than the lesson's length.")
        
    def __str__(self):
        return self.lesson.name + " view by " + str(self.user)