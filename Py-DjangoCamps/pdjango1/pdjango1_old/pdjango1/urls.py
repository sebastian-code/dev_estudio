from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

##urlpatterns = patterns('',
##    # Examples:
##    # url(r'^$', 'pdjango1.views.home', name='home'),
##    # url(r'^pdjango1/', include('pdjango1.foo.urls')),
##
##    # Uncomment the admin/doc line below to enable admin documentation:
##    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
##
##    # Uncomment the next line to enable the admin:
##    url(r'^admin/', include(admin.site.urls)),
##    url(r'^blog/$', 'blog.views.index'),
##    url(r'^blog/(?P<blog_id>\d+)/$', 'blog.views.detail'),
##    url(r'^blog/(?P<blog_id>\d+)/results/$', 'blog.views.results'),
##    url(r'^blog/(?P<blog_id>\d+)/vote/$', 'blog.views.vote'),
##)
urlpatterns = patterns('blog.views',
    url(r'^$', 'index'),
    url(r'^(?P<blog_id>\d+)/$', 'detail'),
    url(r'^(?P<blog_id>\d+)/results/$', 'results'),
    url(r'^(?P<blog_id>\d+)/vote/$', 'vote'),
)
