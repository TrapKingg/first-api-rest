from django.shortcuts import render
from rest_framework import viewsets
from Series.serializers import actorSerializer, serieSerializer
from .models import actor, serie
# Create your views here.
class actorViewSet(viewsets.ModelViewSet):
    queryset = actor.objects.all().order_by('id')
    serializer_class = actorSerializer

class serieViewSet(viewsets.ModelViewSet):
    queryset = serie.objects.all()
    serializer_class = serieSerializer
