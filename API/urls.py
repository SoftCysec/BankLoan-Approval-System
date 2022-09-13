from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('API', views.ApprovalsView)

urlpatterns = [
    path('form/', views.MyForm, name='MyForm'),
    path('api/', include(router.urls)),
    path('status/', views.approvereject),
]