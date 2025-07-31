from django.urls import path
from . import views


urlpatterns = [
    path('student',views.StudentView,name="student")
    
]