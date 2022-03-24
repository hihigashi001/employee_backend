from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import EmployeeViewSet, EmployeeListView, EmployeeRetrieveView


router = routers.DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employees')

urlpatterns = [
    path('list-employee/', EmployeeListView.as_view(), name='list-employee'),
    path('detail-employee/<str:pk>/', EmployeeRetrieveView.as_view(), name='detail-employee'),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
