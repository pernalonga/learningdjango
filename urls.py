from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from blog.models import Artigo
from blog.feeds import UltimosArtigos

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin[/]', include(admin.site.urls)),
    
    (r'^$', 'django.views.generic.date_based.archive_index',
    {'queryset': Artigo.objects.all(),'date_field': 'publicacao'}),

    (r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
    {'feed_dict': {'ultimos': UltimosArtigos}}),
    
)

