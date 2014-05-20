from django import forms
from reference.models import *

class referenceStep1(forms.ModelForm):
	class Meta:
		model = Reference

class referenceStep2(forms.ModelForm):
	class Meta:
		model = Reference_file




