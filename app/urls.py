from django.urls import path, include
from .views import ClientViewset
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('', ClientViewset)
urlpatterns = [
    path('', include(router.urls))
]