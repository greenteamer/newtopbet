from django.conf.urls import patterns, include, url
from newtopbet.views import HomeListView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newtopbet.views.home', name='home'),
    # url(r'^newtopbet/', include('newtopbet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeListView.as_view(), name='home'),
    url(r'^pages/', include('pages.urls', namespace="pages")),
    (r'^ckeditor/', include('ckeditor.urls')),
)
