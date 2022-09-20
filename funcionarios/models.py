from statistics import mode
from django.db import models

class Perfil(models.Model):
    cargo = models.CharField(max_length=60)
    def __str__(self) -> str:
        return self.cargo



class Funcionarios(models.Model):
    nome = models.CharField(max_length=60)
    dataNascimento = models.DateField(max_length=100)
    endereco = models.CharField(max_length=100, null=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT)
    def __str__(self) -> str:
        return self.nome
   
class Departamento(models.Model):
    nome = models.CharField(max_length=60)
    funcionario = models.ManyToManyField(Funcionarios)


