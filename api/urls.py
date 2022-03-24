from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import EmployeeViewSet


router = routers.DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employees')

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
