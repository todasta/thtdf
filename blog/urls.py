from django.conf.urls import patterns, include, url

from views import CategoryView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thtdf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^category/(?P<slug>[-\w]+)/$', CategoryView.as_view()),
)
