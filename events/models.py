# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

	gender = models.CharField(max_length=7,blank =False)

class Events(models.Model):

	event_name = models.CharField(max_length=100, blank=False)
	event_description = models.TextField(blank=False,default='hello')
	event_date = models.DateField(auto_now=False, blank=False)
	users_attend = models.TextField()