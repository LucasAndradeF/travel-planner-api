from rest_framework.views import APIView
from rest_framework.response import Response
from .services import buscar_endereco, buscar_moeda, buscar_destino


class CepView(APIView):
    def get(self, request, cep):
        try:
            dados = buscar_endereco(cep)
            return Response(dados)
        except ValueError as e:
            return Response({"error": str(e)}, status=400)


class CotacaoView(APIView):
    def get(self, request, moeda):
        try:
            dados = buscar_moeda(moeda)
            return Response(dados)
        except ValueError as e:
            return Response({"error": str(e)}, status=400)


class BuscarMoedaView(APIView):
    def get(self, request, pais):
        try:
            dados = buscar_destino(pais)
            return Response(dados)
        except ValueError as e:
            return Response({"error": str(e)}, status=400)
