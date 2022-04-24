from django import forms
from .models import Donor
from django.forms import ModelForm

class AddDonor(ModelForm):
	class Meta:
		model=Donor
		fields='__all__'





