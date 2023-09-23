from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Lesson, LessonView


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'URL', 'length']


class LessonViewSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()

    class Meta:
        model = LessonView
        fields = ['lesson', 'viewedAt', 'viewed']