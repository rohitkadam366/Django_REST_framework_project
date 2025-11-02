from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

router = DefaultRouter()
router.register(r'employees1', EmployeeViewSet, basename='employee')   # bsename= only of ViewSet . ModelViewSet automatically handle 

urlpatterns = [
    path('', include(router.urls)),
]
