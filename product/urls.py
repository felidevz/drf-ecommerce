from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()
router.register(r'category', viewsets.CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls))
]
