from rest_framework import serializers
from .models import TripPlan


class TripPlanCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripPlan
        fields = ['cep_origem', 'data_ida', 'orcamento', 'destino']


class TripPlanReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripPlan
        fields = '__all__'
