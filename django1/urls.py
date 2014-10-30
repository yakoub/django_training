from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name = 'home.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^content/', include('first.urls')),
)
