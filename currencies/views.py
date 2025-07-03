from rest_framework import viewsets
from .models import Currency
from .serializers import CurrencySerializer
from rest_framework.permissions import AllowAny


class CurrencyView(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [AllowAny]
