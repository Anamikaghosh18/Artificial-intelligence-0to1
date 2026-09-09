from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # web api endpoint
    path('students/', include('students.urls')),

    # api endpoint 
    path('api/v1/students/', include('students.urls')), 

    path('api/v1/employees/', include('employees.urls')), 

    path('api/v1/blogs/', include('blogs.urls')),
]
