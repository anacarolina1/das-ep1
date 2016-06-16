from __future__ import unicode_literals

from django.db import models

''' Model consists of the data we need in the application.
	This model has three numbers use to calculate sine, cosine and tangent.'''

class Input(models.Model):

	''' The Input class lists variables representing data as static class attributes.
	    Here is used FloatField to represent a floating-point number. '''
	
	r = models.FloatField()
	r2 = models.FloatField()
	r3 = models.FloatField()