from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.list_students, name='list_students'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('courses/', views.list_courses, name='list_courses'),
    path('courses/add/', views.add_course, name='add_course'),
    path('attendance/', views.mark_attendance, name='mark_attendance'),
    path('attendance/list/', views.list_attendance, name='list_attendance'),
    path('student-form/', views.student_form_view, name='student_form'),
]