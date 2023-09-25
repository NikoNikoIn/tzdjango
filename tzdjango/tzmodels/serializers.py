from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LessonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonView
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    lessonview = LessonViewSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'
