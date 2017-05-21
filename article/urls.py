from django.conf.urls import url

from article import views

urlpatterns = [
  url(r'articles/$', views.ArticleList.as_view(), name='list'),
  url(r'partials/articles/(?P<pk>\d+)/$', views.ArticleView.as_view(), name='view'),
  url(r'articles/create/$', views.ArticleCreate, name='create'),
  url(r'articles/(?P<pk>\d+)/edit$', views.ArticleUpdate, name='update'),
  url(r'articles/(?P<pk>\d+)/delete$', views.ArticleDelete.as_view(), name='delete'),
]
