from django.conf.urls import patterns, include, url
import lyrics

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'samidare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^lyrics/', include('lyrics.urls', namespace="lyrics")),
    url(r'^admin/', include(admin.site.urls)),
)
