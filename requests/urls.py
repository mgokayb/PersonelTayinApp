from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonelViewSet, AdliyeViewSet, TayinTalebiViewSet

router = DefaultRouter()
router.register('personel', PersonelViewSet, basename='personel')
router.register('adliye', AdliyeViewSet, basename='adliye')
router.register('talepler', TayinTalebiViewSet, basename='talepler')

urlpatterns = [
    path('', include(router.urls)),
]