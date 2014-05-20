from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fchingalosite.views.home', name='home'),
    # url(r'^fchingalosite/', include('fchingalosite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

     url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
    
    
)+ staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns = patterns('',
		url(r'^referenceupload/', include('reference.urls')),
		url(r'^reportupload/', include('report.urls')),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT,
        'show_indexes': True}),
        url(r'',
        include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
