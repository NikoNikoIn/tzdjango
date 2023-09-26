from django.shortcuts import render
from django.db.models import Sum

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import *
from .serializers import *


def homePage(request):
    return render(request, 'home.html')


@api_view(['GET'])
def getLessonList(request):
    lessons = Lesson.objects.all()
    serializer = LessonSerializer(lessons, many = True)
    return Response(serializer.data)


#1
@api_view(['GET'])
def getUserLessons(request):
    user = request.user
    lessons = Lesson.objects.filter(inProduct__owner = user)
    serializer = LessonSerializer(lessons, many = True)
    views = LessonView.objects.filter(user = user)
    serializerViews = LessonViewSerializer(views, many = True)
    return Response({'lessons': serializer.data, 'views': serializerViews.data})


#2
@api_view(['GET'])
def getLessonsByProduct(request, pk):
    user = request.user

    try:
        product = Product.objects.get(name=pk)
        lessons = Lesson.objects.filter(inProduct__name = product, inProduct__owner = user)
        views = LessonView.objects.filter(user = user, lesson__in = lessons)
        serializer = LessonSerializer(lessons, many = True)
        serializerViews = LessonViewSerializer(views, many = True)
        return Response({'lessons': serializer.data, 'views': serializerViews.data})
    except:
        return Response({'detail':'Product does not exist or you are not authorized'}, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET'])
def getProductStats(request):
    products = Product.objects.all()
    product_stats = []

    for product in products:
        lessons = Lesson.objects.filter(inProduct=product)
        lesson_views = LessonView.objects.filter(lesson__in=lessons)

        total_lessons_viewed = lesson_views.count()
        total_time_spent = lesson_views.aggregate(Sum('viewedTime'))['viewedTime__sum']
        total_students = product.owner.count()
        total_users = User.objects.count()

        product_stat = {
            'product': product.name,
            'total_lessons_viewed': total_lessons_viewed,
            'total_time_spent': total_time_spent,
            'total_students': total_students,
            'product_conversion_rate': (total_students / total_users) * 100
        }

        product_stats.append(product_stat)

    return Response(product_stats)