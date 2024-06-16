from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Kategorija(models.Model):
    name = models.CharField(max_length=20)
    opis = models.CharField(max_length=20)
    aktivna = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Produkt(models.Model):
    name = models.CharField(max_length=20)
    opis = models.CharField(max_length=20)
    kategorija = models.ForeignKey(Kategorija, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    cena = models.IntegerField()
    kolicina = models.IntegerField()

    def __str__(self):
        return self.name


class Klient(models.Model):
    name = models.CharField(max_length=20)
    prezime = models.CharField(max_length=20)
    adresa = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Prodazba(models.Model):
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    datum = models.DateField()
    kolicina=models.IntegerField()
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.produkt.name}-{self.klient.name}"