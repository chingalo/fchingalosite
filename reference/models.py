from django.db import models
from cms.models.pluginmodel import CMSPlugin

class Reference(models.Model):
	reference_title = models.CharField(max_length=200)
	reference_title_discription = models.TextField(max_length=2000, blank=True)
	
	#refernces categories
	category_choice = (
	('Finance','Finance'),
	('Institution','Institution'),
	('Social','Social'),
	('Others','Others'),	
	)
	reference_category = models.CharField(max_length=200, choices = category_choice , default = 'Finance')
		
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.reference_title
        
class Reference_file(models.Model):
	reference_title = models.ForeignKey('Reference', on_delete=models.CASCADE)
	name_of_file = models.CharField(max_length=200 )
	date_of_upload_reference = models.DateField('date of event')
	reference_file = models.FileField(upload_to='references')
	
	def __unicode__(self): # Python 3: def __str__(self):
		return self.name_of_file
		

