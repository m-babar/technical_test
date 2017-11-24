# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions,viewsets
from .models import Pet
# from rest_framework.generics import CreateAPIView

from .serializers import PetSerializer

class PetView(viewsets.ModelViewSet):
    """ 
        Only Authenticate User perform CRUD Operations
    """
    permission_classes = (permissions.IsAuthenticated,)
    model = Pet
    serializer_class = PetSerializer

    def get_queryset(self):
        """ Return pets belonging to the current user(owner) """
        queryset = self.model.objects.all()
        # filter to pets owned by owner making request
        queryset = queryset.filter(owner=self.request.user)
  
        return queryset
  
    def perform_create(self, serializer):
        """ Associate current user as pet owner """
        return serializer.save(owner=self.request.user)
