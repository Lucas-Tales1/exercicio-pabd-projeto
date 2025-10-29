from django.shortcuts import render
from rest_framework import viewsets
from .models import Projeto, Tarefa
from .serializers import ProjetoSerializer, TarefaSerializer

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

# Create your views here.

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer 



class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer 

