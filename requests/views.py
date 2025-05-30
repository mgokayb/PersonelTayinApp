from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Personel, Adliye, TayinTalebi
from .serializers import PersonelSerializer, AdliyeSerializer, TayinTalebiSerializer

class PersonelViewSet(viewsets.ModelViewSet):
    queryset = Personel.objects.all().order_by('sicil_no')
    serializer_class = PersonelSerializer
    pagination_class = None

class AdliyeViewSet(viewsets.ModelViewSet):
    queryset = Adliye.objects.all().order_by('isim')
    serializer_class = AdliyeSerializer
    pagination_class = None

class TayinTalebiViewSet(viewsets.ModelViewSet):
    queryset = TayinTalebi.objects.all().order_by('-olusturma_tarihi')
    serializer_class = TayinTalebiSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ['talep_turu']
    search_fields = ['personel__sicil_no', 'tercih_adliye__isim', 'aciklama']
    ordering_fields = ['olusturma_tarihi']