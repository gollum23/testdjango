from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# Alt + 94 = ^
from django.contrib import admin
admin.autodiscover()
handler404 = 'semanario.views.custom404'

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'semanario.views.index', name='home'),
    url(r'^(?P<num>\d+)/$','semanario.views.index'),
    url(r'^(?P<num>\d+)/articulo(?P<article>\d+)/$','semanario.views.article'),
    url(r'^(?P<num>\d+)/humor/$','semanario.views.humor'),

    # url(r'^svch/', include('svch.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # Url para incluir el ckeditor
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT,})

)
