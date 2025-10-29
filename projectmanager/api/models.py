from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nome = models.CharField(max_length=50)

class Projeto(models.Model):
    usuario = models.ForeingKey(Usuario)
    nome = models.CharField(max_length=50)

class Tarefa(models.Model):
    projeto = models.ForeignKey(Projeto)
    nome = models.CharField(max_length=50)
