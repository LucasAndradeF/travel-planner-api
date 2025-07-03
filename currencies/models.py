from django.db import models


class Currency(models.Model):
    pais = models.CharField(max_length=255, unique=True)
    moeda = models.CharField(max_length=255)
    codigo_iso = models.CharField(max_length=3)
