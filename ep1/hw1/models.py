from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm


class Input(models.Model):
    r = models.FloatField()

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = "__all__" 

 