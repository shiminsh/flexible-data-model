from django import forms
from django.contrib import auth
from django.forms import ModelForm
from patient.models import *
from eav.forms import BaseDynamicEntityForm

class RegistrationForm(forms.ModelForm):

	class Meta:
		# Set this form to use the model
		model = Register
		

class DiseaseForm(BaseDynamicEntityForm):

	class Meta:
		# Set this form to use the model
		model = Disease

		# Exclude these fields of form
		exclude = ('patient',)