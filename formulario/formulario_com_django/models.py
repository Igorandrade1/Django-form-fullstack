from django.db import models


# Create your models here.

class Formulario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    sexo = models.CharField(max_length=1)
    endereco = models.CharField(max_length=150)
    cpf = models.IntegerField()


