from django.conf.urls import patterns, url

from report import views

urlpatterns = patterns('',
    url(r'^$', views.reportStep1, name='reportStep1'),
    #url(r'step1^$', views.reportStep2, name='reportStep2'),
    #url(r'step1^$', views.reportStep3, name='reportStep3'),

#url(r'step1^$', views.authorize, name='authorize'),
)
