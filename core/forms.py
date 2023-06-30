from django import forms
from .models import ControleVisitante, ControleChave, ControleVeiculo, SetorChave, SetorVeiculo

class ControleVisitanteForm(forms.ModelForm):
    class Meta:
        model = ControleVisitante
        fields = ("registro_entrada", "nome","cpf", "placa_carro", "empresa", "nota_fiscal", "registro_saida", "observacao", "autorizacao",)


class ControleChaveForm(forms.ModelForm):
    class Meta:
        model = ControleChave
        fields = ('setor', 'registro_entrega', 'registro_recebimento', 'funcionario', 'matricula',)


class SetorChaveForm(forms.ModelForm):
    class Meta:
        model = SetorChave
        fields = '__all__'


class ControleVeiculoForm(forms.ModelForm):
    class Meta:
        model = ControleVeiculo
        fields = ('nome','setor', 'registro_entrada', 'registro_saida',)


class SetorVeiculoForm(forms.ModelForm):
    class Meta:
        model = SetorVeiculo
        fields = '__all__'