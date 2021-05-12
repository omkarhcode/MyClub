from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Venue

# Create a venue form
class VenueForm(ModelForm):
	class Meta:
		model = Venue
		# fields = '__all__'
		fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')

		# RND on how to add class: to labels
		labels = {
			'name': '', 
			'address': '', 
			'zip_code': '', 
			'phone': '', 
			'web': '', 
			'email_address': '' 			
		}

		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venur Name'}), 
			'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}), 
			'zip_code': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}), 
			'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}), 
			'web': forms.URLInput(attrs={'class':'form-control', 'placeholder':'Web Address'}), 
			'email_address': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'})
		}
