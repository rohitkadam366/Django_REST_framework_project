from django.urls import path
from . import views


urlpatterns = [
    path('',views.student_view,name="student"),
    path('<int:pk>',views.StudentDetailsView,name="StudentDetailsView"),

]