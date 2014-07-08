from django.db import models
from cms.models.pluginmodel import CMSPlugin
 
class Contacts(models.Model):
	first_name = models.CharField(max_length=200)
	middle_name = models.CharField(max_length=200, blank=True)
	surname = models.CharField(max_length=200)
	e_mail = models.EmailField(max_length=200,  blank=True)
	mobile_phone = models.CharField(max_length=2000, blank=True)
	location = models.CharField(max_length=200, blank=True)
	duty = models.TextField(max_length=2000, blank=True)
	message = models.TextField(max_length=20000000, blank=True)
	
	def __unicode__(self):   # Python 3: def __str__(self):
		return self.first_name

class ContactsPlugin(CMSPlugin):
	title=models.CharField(max_length=200, default='contacts')
class ServicesPlugin(CMSPlugin):
	title = models.CharField(max_length=200, default='services')
