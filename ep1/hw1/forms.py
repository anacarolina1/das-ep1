from django import forms
from models import Input

class InputForm(forms.ModelForm):

	''' The InputForm class show a generic form across 
	    applications if we by convention apply the name Input 
	    for the class holding the data. '''

	class Meta:
		model = Input
		fields = '__all__'

