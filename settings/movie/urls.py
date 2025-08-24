from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('directors', DirectorViewSet)
router.register('countries', CountryViewSet)
router.register('actors', ActorViewSet)

urlpatterns = [
    path('', include(router.urls))
]