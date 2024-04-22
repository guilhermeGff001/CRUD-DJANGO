from django.db import models

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    sobrenome = models.CharField(max_length=100, null=False, blank=False)
    data_de_nascimento = models.DateField()
    cargo = models.CharField(max_length=100, null=False, blank=False)
    salario = models.IntegerField(null=False, blank=False)
    data_de_admissao = models.DateField(auto_now_add=True, null=False, blank=False)