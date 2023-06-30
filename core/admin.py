from django.contrib import admin
from .models import ControleChave, ControleVeiculo, ControleVisitante, SetorChave, SetorVeiculo
# Register your models here.

@admin.register(ControleChave)
class ControleChaveAdmin(admin.ModelAdmin):
    list_display = ('setor', 'registro_entrega', 'registro_recebimento', 'funcionario', 'matricula', 'porteiro',)


@admin.register(ControleVisitante)
class ControleVisitanteAdmin(admin.ModelAdmin):
    list_display = ('registro_entrada', 'nome', 'cpf', 'placa_carro', 'empresa', 'nota_fiscal', 'registro_saida', 'observacao', 'porteiro')


@admin.register(SetorVeiculo)
class SetorVeiculoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(SetorChave)
class SetorChaveAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(ControleVeiculo)
class ControleVeiculoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'setor', 'registro_entrada', 'registro_saida', 'porteiro')
