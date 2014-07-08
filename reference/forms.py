from django import forms
from reference.models import *

class referenceStep1Form(forms.ModelForm):
	class Meta:
		model = Reference

class referenceStep2Form(forms.ModelForm):
	class Meta:
		model = Reference_file




