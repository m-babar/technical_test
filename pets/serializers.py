from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    owner  = serializers.CharField(source='owner.username',read_only=True)
    
    class Meta:
        model = Pet
        fields = ('owner', 'name', 'pet_type', 'birthday')
