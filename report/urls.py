from django.conf.urls import patterns, url

from report import views

urlpatterns = patterns('',
    url(r'^$', views.reportUploadStep1, name='reportStep1'),
    url(r'^step2$', views.reportUploadStep2, name='reportStep2'),
    url(r'^step3$', views.reportUploadStep3, name='reportStep3'),

#url(r'step1^$', views.authorize, name='authorize'),
)
