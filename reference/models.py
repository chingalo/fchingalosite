from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils import timezone

class Reference(models.Model):
	reference_title = models.CharField(max_length=200)

	#refernces categories
	category_choice = (
	('Business Plan','Business Plan'),
	('Business Records & Financial Management ','Business Records & Financial Management '),
	('Business Skills & Entrepreneurship Development Training','Business Skills & Entrepreneurship Development Training'),
	('Evaluation and Impact Assessment ','Evaluation and Impact Assessment '),
	('Financial & Economic Analysis','Financial & Economic Analysis'),
	('Institutional & Organizational development ','Institutional & Organizational development '),
	('Legal Framework','Legal Framework'),
	('Microfinance Best Practices','Microfinance Best Practices'),
	('Project Management','Project Management'),
	('Project Management ','Project Management '),
	('Socio- Economic Studies','Socio- Economic Studies'),
	('Training & Capacity Building','Training & Capacity Building'),
	('Waste Management','Waste Management'),
	('Water Supply Management','Water Supply Management'),	
	)
	reference_category = models.CharField(max_length=200, choices = category_choice , default = 'Business Plan')
	reference_title_discription = models.TextField(max_length=2000, blank=True)
		
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.reference_title
        
class Reference_file(models.Model):
	reference_title = models.ForeignKey('Reference', on_delete=models.CASCADE)
	name_of_file = models.CharField(max_length=200 )
	date_of_upload_reference = models.DateField('date for upload file',default=timezone.now)
	reference_file = models.FileField(upload_to='references')
	
	def __unicode__(self): # Python 3: def __str__(self):
		return self.name_of_file
		

