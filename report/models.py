from django.db import models
from cms.models.pluginmodel import CMSPlugin

class Receiver_of_report(models.Model):
	name_of_receiver = models.CharField(max_length=200)
	e_mail = models.EmailField(max_length=200,  blank=True)
	mobile_phone_number = models.CharField(max_length=200,  blank=True)
	location_or_address	= models.CharField(max_length=200,  blank=True)
	
	
	def __unicode__(self):	# Python 3: def __str__(self):
		return self.name_of_receiver
	
class Details_of_Report(models.Model):
	name_of_receiver = models.ForeignKey('Receiver_of_report', on_delete=models.CASCADE)
	report_title = models.CharField(max_length=200)
	description_of_report = models.TextField(max_length=200000, blank=True)
	date_of_submission = models.DateField('date of event')
	
	def __unicode__(self):	# Python 3: def __str__(self):
		return self.report_title

class Report_files(models.Model):
	report_title = models.ForeignKey('Details_of_report', on_delete=models.CASCADE)	
	report_file = models.FileField(upload_to='reports')
	name_of_report_file = models.CharField(max_length=200)
	
	def __unicode__(self):	# Python 3: def __str__(self):
		return self.name_of_report_file
	
#class ContactsPlugin(CMSPlugin):
	#title=models.CharField(max_length=200, default='contacts ')
