from rest_framework import serializers
from .models import Personel, Adliye, TayinTalebi

class PersonelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personel
        fields = ['id', 'sicil_no', 'user']
        read_only_fields = ['id']

class AdliyeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adliye
        fields = ['id', 'isim']
        read_only_fields = ['id']

class TayinTalebiSerializer(serializers.ModelSerializer):
    personel = serializers.PrimaryKeyRelatedField(queryset=Personel.objects.all())
    tercih_adliye = serializers.PrimaryKeyRelatedField(queryset=Adliye.objects.all())
    personel_detay = PersonelSerializer(source='personel', read_only=True)
    adliye_detay = AdliyeSerializer(source='tercih_adliye', read_only=True)

    class Meta:
        model = TayinTalebi
        fields = [
            'id', 'personel', 'personel_detay',
            'tercih_adliye', 'adliye_detay',
            'talep_turu', 'aciklama', 'olusturma_tarihi'
        ]
        read_only_fields = ['id', 'personel_detay', 'adliye_detay', 'olusturma_tarihi']