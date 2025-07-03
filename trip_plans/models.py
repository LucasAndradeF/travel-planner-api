from django.db import models
from uuid import uuid4
from django.contrib.auth import get_user_model

User = get_user_model()


class TripPlan(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='trip_plans')
    cep_origem = models.CharField(max_length=8)
    origem_cidade = models.CharField(max_length=150)
    origem_estado = models.CharField(max_length=150)
    data_ida = models.DateField()
    orcamento = models.DecimalField(max_digits=10, decimal_places=2)
    moeda_destino = models.CharField(max_length=10)
    cotacao = models.JSONField()
    data_criacao = models.DateTimeField(auto_now_add=True)
