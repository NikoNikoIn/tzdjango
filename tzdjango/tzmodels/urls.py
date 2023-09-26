from django.urls import path
from .views import *

urlpatterns = [
    path('lessons/', getLessonList),
    path('userlessons/', getUserLessons),
    path('productlessons/<str:pk>/', getLessonsByProduct),
    path('productstats/', getProductStats),
]