from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('update/<int:student_id>/',views.update_student, name='update_student'),
]