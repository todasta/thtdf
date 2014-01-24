from django.conf.urls import patterns, include, url

from django.contrib import admin
import thtdf.settings as settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thtdf.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

