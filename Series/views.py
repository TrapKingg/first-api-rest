from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Series.serializers import actorSerializer, serieSerializer
from .models import actor, serie
from django.http import Http404
from .permissions import IsOwnerOrReadOnly
#Create your views here.
class actorViewSet(viewsets.ModelViewSet):
    queryset = actor.objects.all().order_by('id')
    serializer_class = actorSerializer
    permission_classes = (IsOwnerOrReadOnly, )

class serieViewSet(viewsets.ModelViewSet):
    queryset = serie.objects.all()
    serializer_class = serieSerializer
    permission_classes = (IsOwnerOrReadOnly, )
