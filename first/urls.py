from django.conf.urls import patterns,url

from first import views

urlpatterns = patterns('',
  url(r'first/$', views.FirstList.as_view(), name='first-list'),
  url(r'first/(?P<pk>\d+)/$', views.FirstView.as_view(), name='first-view'),
  url(r'first/create/$', views.FirstCreate.as_view(), name='first-create'),
  url(r'first/(?P<pk>\d+)/edit$', views.FirstUpdate.as_view()),
  url(r'first/(?P<pk>\d+)/delete$', views.FirstDelete.as_view()),
)
