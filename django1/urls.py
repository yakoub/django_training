from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = i18n_patterns('',
    # Examples:
    # url(r'^$', 'django1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name = 'home.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),

#    url(r'^account/', include('account.urls', namespace='account')),
#    url(r'^account/', include('django.contrib.auth.urls')),

    url(r'^content/?$', TemplateView.as_view(template_name = 'content.html'), name='content'),
    url(r'^content/', include('first.urls', namespace='first')),
    url(r'^content/', include('actors.urls', namespace='actors')),
    url(r'^content/', include('article.urls', namespace='articles')),
)
