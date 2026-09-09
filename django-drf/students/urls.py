from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.home, name = 'students-home'),

    path('student-details/', views.studentView, name = 'students-details'),

    path('student/<int:pk>/', views.studentDetailView, name = 'student-details'), 
]