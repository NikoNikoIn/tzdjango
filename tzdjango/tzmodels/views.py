from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from .models import *
from .serializers import *


@api_view(['GET'])
def getLessonList(request):
    lessons = Lesson.objects.all()
    serializer = LessonSerializer(lessons, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def getUserLessons(request):
    user = request.user
    lessons = Lesson.objects.filter(inProduct__owner=user)
    serializer = LessonSerializer(lessons, many=True)
    views = LessonView.objects.filter(user=user)
    serializerViews = LessonViewSerializer(views, many = True)
    return Response({'lessons': serializer.data, 'products': serializerViews.data})