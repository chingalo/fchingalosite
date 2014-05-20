from django import forms
from report.models import *

class reportStep1Form(forms.ModelForm):
	class Meta:
		model = Receiver_of_report

class reportStep2Form(forms.ModelForm):
	class Meta:
		model = Details_of_Report
		
class reportStep3Form(forms.ModelForm):
	class Meta:
		model = Report_files		
