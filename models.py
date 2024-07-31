from django.db import models

class Pessoa(models.Model):
    Cpf = models.FloatField()
    NomeCompleto = models.CharField(max_length=50)
    Email=models.CharField(max_length=75)
    Telefone_celular=models.IntegerField() 
