from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class CepView(APIView):
    def get(self, request, cep):
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if response.status_code == 200:
            data = response.json()
            dados_cep = {
                "cidade": data.get("localidade"),
                "estado": data.get("estado")
            }
            return Response(dados_cep)
        return Response({"error": "CEP inválido ou não encontrado."}, status=400)


class CotacaoView(APIView):
    def get(self, request, moeda):
        response = requests.get(f'https://economia.awesomeapi.com.br/last/{moeda}')
        if response.status_code == 200:
            dados = response.json()
            dados_cotacao = {
                "moeda_local": dados.get("BRLUSD").get("codein"),
                "valor": dados.get("BRLUSD").get("high"),
            }
            return Response(dados_cotacao)
        return Response({"error"})
