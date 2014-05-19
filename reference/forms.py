from django import forms
from cms.models.pluginmodel import CMSPlugin
from reference.models import *

class referenceForm(forms.ModelForm):
	class Meta:
		model = Reference_file

class ReferenceFormPlugin(CMSPlugin):
	title=models.CharField(max_length=200, default='test fro form')
