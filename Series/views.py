from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework import status
from Series.serializers import actorSerializer, serieSerializer, UserSerializer
from .models import actor, serie
from django.http import Http404
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework import permissions
#Create your views here.

class actorViewSet(viewsets.ModelViewSet):
    queryset = actor.objects.all().order_by('id')
    serializer_class = actorSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly, )
    #########################
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        #########################################

class serieViewSet(viewsets.ModelViewSet):
    queryset = serie.objects.all()
    serializer_class = serieSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly, )
    ##############################################
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        ##########################################

#############################->ESTO SE BORRA SI NO FUNCIONA
class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)
