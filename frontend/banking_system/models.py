# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

	user = models.OneToOneField(User)

	address = models.TextField(blank=True)
	phone_num = models.TextField(blank=True)

	def __str__(self):
		return self.user.username
