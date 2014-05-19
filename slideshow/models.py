from cms.models.pluginmodel import CMSPlugin
from django.db import models

# Create your models here.
class SlideshowHome(models.Model):
    image = models.ImageField(upload_to='carousel')
    desc_title = models.CharField(max_length=200,default='')
    desc_text = models.CharField(max_length=500,default='')
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.desc_title

class SlideshowReference(models.Model):
    image = models.ImageField(upload_to='carousel')
    desc_title = models.CharField(max_length=200,default='')
    desc_text = models.CharField(max_length=500,default='')
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.desc_title        

class SlideshowReport(models.Model):
    image = models.ImageField(upload_to='carousel')
    desc_title = models.CharField(max_length=200,default='')
    desc_text = models.CharField(max_length=500,default='')
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.desc_title
        
class SlideshowSearch(models.Model):
    image = models.ImageField(upload_to='carousel')
    desc_title = models.CharField(max_length=200,default='')
    desc_text = models.CharField(max_length=500,default='')
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.desc_title 
               
class SlideshowHomePlugin(CMSPlugin):
    title = models.CharField(max_length=200,default='home page slide show')
    
class SlideshowReferencePlugin(CMSPlugin):
    title = models.CharField(max_length=200,default='reference page slide show')
    
class SlideshowReportPlugin(CMSPlugin):
    title = models.CharField(max_length=200,default='report page slide show')    

class SlideshowSearchPlugin(CMSPlugin):
    title = models.CharField(max_length=200,default='search page slide show')
