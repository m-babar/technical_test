# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    PET_TYPE = (
        ('D', 'Dog'),
        ('C', 'Cat'),
    )
    
    name = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    pet_type = models.CharField(max_length=1, choices=PET_TYPE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return "%s :: %s" % (self.name, self.pet_type)
