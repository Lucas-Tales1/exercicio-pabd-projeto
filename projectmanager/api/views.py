from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, Projeto, Tarefa
from .serializers import UsuarioSerializer, ProjetoSerializer, TarefaSerializer

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer 



class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer 

