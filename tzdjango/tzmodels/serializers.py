from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    def get_owner(self, obj):
        return [owner.username for owner in obj.owner.all()]
    
    class Meta:
        model = Product
        fields = '__all__'


class LessonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonView
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    lessonview = LessonViewSerializer(many=True, read_only=True)
    inProduct = serializers.SerializerMethodField()

    def get_inProduct(self, obj):
        return [product.name for product in obj.inProduct.all()]

    class Meta:
        model = Lesson
        fields = '__all__'
