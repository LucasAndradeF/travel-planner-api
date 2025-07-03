from rest_framework import viewsets
from .serializers import TripPlanCreateSerializer, TripPlanReadSerializer
from .models import TripPlan
from integrations.services import buscar_endereco, buscar_moeda
from rest_framework.permissions import IsAuthenticated


class TripPlanView(viewsets.ModelViewSet):
    queryset = TripPlan.objects.all()
    serializer_class = TripPlanReadSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return TripPlanCreateSerializer
        return TripPlanReadSerializer

    def perform_create(self, serializer):
        cep = self.request.data.get("cep_origem")
        destino = self.request.data.get("destino")

        endereco = buscar_endereco(cep)         
        cotacao = buscar_moeda(destino)     

        serializer.save(
            user=self.request.user,
            origem_cidade=endereco["cidade"],
            origem_estado=endereco["estado"],
            cotacao=cotacao,
            moeda_destino=cotacao["moeda"],
            destino=destino
    )
