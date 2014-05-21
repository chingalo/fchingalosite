from django.conf.urls import patterns, url

from reference import views
urlpatterns = patterns('',
    url(r'^referenceupload/$', views.referenceUploadStep1, name='referenceStep1'),
    url(r'^referenceupload/step2$', views.referenceUploadStep2, name='referenceStep2'),
    
    
    
    )
