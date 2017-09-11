# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

	gender = models.CharField(max_length=7,blank =False)

class Events(models.Model):

	event_name = models.CharField(max_length=100, blank=False)
	event_description = models.TextField(blank=False,default='hello')
	event_date = models.DateField(auto_now=False, blank=False)
	event_price = models.DecimalField(max_digits=7, decimal_places=2,blank=False,default= 1000.00)
	users_bought = models.TextField()
	users_attend = models.TextField()