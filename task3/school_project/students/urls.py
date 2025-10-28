from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student-list'),
    path('students/adults/', views.adult_students, name='adult-students'),
]
