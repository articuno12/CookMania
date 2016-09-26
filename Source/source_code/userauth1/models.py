from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
	MERCHANT = 'ME'
	USER = 'US'
	user = models.OneToOneField(User)
	APPLYING_AS_A = (
        (MERCHANT, 'Merchant'),
        (USER, 'User'),
	)
	applying_as_a = models.CharField(
        max_length=2,
        choices=APPLYING_AS_A,
        default=USER,)
	
	
    	def __unicode__(self):
        	return self.user.username

	def is_upperclass(self):	
		return self.applying_as_a in (self.MERCHANT)
