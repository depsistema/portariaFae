from django.urls import path
from .views import visitante, finalizarSaida, controleChave, finalizarEntregaChave, controleVeiculo, finalizarSaidaVeiculo

urlpatterns = [
    path('', visitante, name='visitante'),
    path('finalizarSaidaVisitante/', finalizarSaida, name='finalizar_saida'),
    path('controlechave/', controleChave, name="controle_chave"),
    path('finalizarEntregaChave/', finalizarEntregaChave, name='finalizar_entrega_chave'),
    path('controleVeiculo/', controleVeiculo, name='controle_veiculo'),
    path('finalizarSaidaVeiculo/', finalizarSaidaVeiculo, name='finalizar_saida_veiculo')
]