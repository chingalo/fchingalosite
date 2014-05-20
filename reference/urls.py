from django.conf.urls import patterns, url

from reference import views
urlpatterns = patterns('',
    url(r'^$', views.referenceStep1, name='referenceStep1'),
    #url(r'step2^$', views.referenceStep2, name='referenceStep2'),
    
    
    
    )
