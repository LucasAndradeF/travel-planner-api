from django.urls import path
from .views import CepView, CotacaoView, BuscarMoedaView


urlpatterns = [
    path('cep/<str:cep>/', CepView.as_view(), name='buscar-cep'),
    path('moeda/<str:moeda>/', CotacaoView.as_view(), name='buscar-moeda'),
    path('pais/<str:pais>/', BuscarMoedaView.as_view(), name='buscar-moeda'),
]
