from django.conf.urls import patterns, url

from report import views

urlpatterns = patterns('',
    url(r'^reportupload/$', views.reportUploadStep1, name='reportStep1'),
    url(r'^reportupload/step2$', views.reportUploadStep2, name='reportStep2'),
    url(r'^reportupload/step3$', views.reportUploadStep3, name='reportStep3'),
    url(r'^download/$', views.reportDownload, name='reportDownload'),
    url(r'^search/$', views.reportSearch, name='reportSearch'),

#url(r'step1^$', views.authorize, name='authorize'),
)
