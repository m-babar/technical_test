# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PetSerializer, SignupSerializer, LoginSerializer, LogoutSerializer
from .models import Pet



def dashboard(request):
    return render(request, 'pets/dashboard.html')


@login_required
def my_pets(request):
    mypets = Pet.objects.filter(owner=request.user)
    return render(request, 'pets/my_pets.html', {'mypets':mypets})

# @login_required
class PetView(APIView):
    """ 
        Only Authenticate User perform CRUD Operations
    """
    permission_classes = (IsAuthenticated,)
    model = Pet
    serializer_class = PetSerializer

    def get(self, request, pk=None):
      userdata = self.model.objects.all()
      if pk != None:
        userdata = userdata.filter(id= pk)
      else:
        userdata = userdata.filter(owner=self.request.user)
      serializer = PetSerializer(userdata, many=True)
      return Response(serializer.data)  

    def post(self, request):
      serializer = PetSerializer(data= request.data )
      serializer.is_valid(raise_exception=True)
      serializer.save(owner=self.request.user)
      return Response(serializer.data)

    def put(self, request, pk):
      userdata = Pet.objects.get(pk= pk)
      serializer = PetSerializer(userdata, data=request.data, partial=True)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors)

    def delete(self, request, pk=None):
      self.model.objects.get(pk= pk).delete()
      return Response({
        "status": 202,
        "success" : True,
        "message" : "Successfully Deleted.",
         })


''' Signup '''
class Signup(APIView):
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer

    def post(self, request):

        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception=True):

          user = serializer.save()

          username = user.username
          raw_password = user.password
          #again set password in HASH format
          user.set_password(raw_password)

          user.save()
          
          user = authenticate(username=username, password=raw_password)
          
          token, created = Token.objects.get_or_create(user=user) 
      
          headers = { 'access_token': token.key }
          return Response({
            "status": status.HTTP_201_CREATED,
            "success" : True,
            "message" : "Successfully Created Your Account.",
          }, headers= headers )
        return Response(serializer.errors)


class Login(APIView):
  """
  IT's user login view. accepted method post. it's return always new token. and endpoint is /login.
  """
  permission_classes = (AllowAny,)
  serializer_class = LoginSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(data=request.data)

    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    try:
      token, created = Token.objects.get_or_create(user=user)
      # UserDesktop.as_view()

    except Exception as e:
      pass
      
    headers = {
           'access_token' : token.key
           # 'Access-Control-Expose-Headers': 'access_token'
       }

    return Response({
      "status": status.HTTP_200_OK,
      "message" : 'Successfully login.'
      
    }, headers=headers)


''' Logout ''' 
class Logout(APIView):
  permission_classes = (AllowAny,)
  serializer_class = LogoutSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(data = request.data)
    serializer.is_valid(raise_exception=True)
    token = serializer.validated_data['token']
    if token:
      token.delete()
    else:
      pass

    return Response({
      "status": status.HTTP_200_OK,
      "message" : 'Successfully logout.'
      })



