from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.save_student, name='add_teacher'),
]