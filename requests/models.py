from django.db import models
from django.contrib.auth.models import User

class Personel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sicil_no = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.sicil_no} — {self.user.get_full_name()}"

class Adliye(models.Model):
    isim = models.CharField(max_length=200)

    def __str__(self):
        return self.isim

class TayinTalebi(models.Model):
    TIP_SECENEKLERI = [
        ('il_ici', 'İl İçi'),
        ('il_disi', 'İl Dışı'),
    ]
    personel = models.ForeignKey(Personel, on_delete=models.CASCADE, related_name='talepler')
    tercih_adliye = models.ForeignKey(Adliye, on_delete=models.CASCADE)
    talep_turu = models.CharField(max_length=20, choices=TIP_SECENEKLERI)
    aciklama = models.TextField(blank=True)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.personel.sicil_no} → {self.get_talep_turu_display()}"