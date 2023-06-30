from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ControleVisitante(models.Model):
    registro_entrada = models.DateTimeField()
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    placa_carro = models.CharField(max_length=7, null=True, blank=True)
    empresa = models.CharField(max_length=50, null=True, blank=True)
    nota_fiscal = models.CharField(max_length=10, null=True, blank=True)
    registro_saida = models.DateTimeField(null=True, blank=True)
    observacao = models.CharField(max_length=255, null=True, blank=True)
    autorizacao = models.CharField(max_length=50, null=True, blank=True)
    porteiro = models.ForeignKey(User, on_delete=models.PROTECT)


class SetorVeiculo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class ControleVeiculo(models.Model):
    nome = models.CharField(max_length=100)
    setor = models.ForeignKey(SetorVeiculo, on_delete=models.CASCADE)
    registro_entrada = models.DateTimeField()
    registro_saida = models.DateTimeField(null=True, blank=True)
    porteiro = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome} - {self.setor}"
    
    
class SetorChave(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class ControleChave(models.Model):
    setor = models.ForeignKey(SetorChave, on_delete=models.CASCADE)
    registro_entrega = models.DateTimeField()
    registro_recebimento = models.DateTimeField(null=True, blank=True)
    funcionario = models.CharField(max_length=100)
    matricula = models.CharField(max_length=10)
    porteiro = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.setor



