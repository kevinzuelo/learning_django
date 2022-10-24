import email
from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class User(models.Model):
    objects = models.Manager()
    
    first_name = models.CharField(max_length=100, unique = False)
    last_name = models.CharField(max_length=200, unique = False)
    email = models.EmailField(max_length=264, unique = True)
    
    def __str__(self):
        return "{first}, {last}, {email}".format(first = self.first_name, last = self.last_name, email = self.email)
    