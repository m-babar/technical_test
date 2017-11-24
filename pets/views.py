# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from rest_framework import permissions,viewsets
from .models import Pet
# from rest_framework.generics import CreateAPIView

from .serializers import PetSerializer

def dashboard(request):
	return render(request, 'pets/dashboard.html')


@login_required
def my_pets(request):
	mypets = Pet.objects.filter(owner=request.user)
	return render(request, 'pets/my_pets.html', {'mypets':mypets})


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
