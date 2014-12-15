from django.conf.urls import patterns,url

from article import views

urlpatterns = patterns('',
  url(r'articles/$', views.ArticleList.as_view(), name='list'),
  url(r'partials/articles/slider/(?P<pk>\d+)/$', views.ArticleView.as_view(), name='view'),
  url(r'partials/articles/scroller/(?P<pk>\d+)/$', views.ArticleView.as_view(), name='view'),
  url(r'articles/create/$', views.ArticleCreate, name='create'),
  url(r'articles/(?P<pk>\d+)/edit$', views.ArticleUpdate, name='update'),
  url(r'articles/(?P<pk>\d+)/delete$', views.ArticleDelete.as_view(), name='delete'),
)
