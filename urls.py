from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from blog.models import Artigo

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learningdjango.views.home', name='home'),
    # url(r'^learningdjango/', include('learningdjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin[/]', include(admin.site.urls)),
    
    (r'^$', 'django.views.generic.date_based.archive_index',
    {'queryset': Artigo.objects.all(),'date_field': 'publicacao'}),
)

