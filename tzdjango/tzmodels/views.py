from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from .models import *
from .serializers import *


@api_view(['GET'])
def getLessons(request):
    lessons = Lesson.objects.all()
    serializer = LessonSerializer(lessons, many = True)
    return Response(serializer.data)


