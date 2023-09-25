from django.urls import path
from .views import getLessonList

urlpatterns = [
    path('lessons/', getLessonList),
]