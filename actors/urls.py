from django.conf.urls import patterns,url

from actors import views

urlpatterns = patterns('',
  url(r'actor/$', views.ActressList.as_view(), name='list'),
  url(r'actor/(?P<pk>\d+)/$', views.ActressView.as_view(), name='view'),
  url(r'actor/create/$', views.ActressCreate.as_view(), name='create'),
  url(r'actor/(?P<pk>\d+)/edit$', views.ActressUpdate.as_view()),
  url(r'actor/(?P<pk>\d+)/delete$', views.ActressDelete.as_view()),

  url(r'award/$', views.AwardsList.as_view(), name='award-list'),
  url(r'award/(?P<pk>\d+)/$', views.AwardView.as_view(), name='award-view'),
  url(r'award/create/$', views.AwardCreate.as_view(), name='award-create'),
  url(r'award/(?P<pk>\d+)/edit$', views.AwardUpdate.as_view()),
  url(r'award/(?P<pk>\d+)/delete$', views.AwardDelete.as_view()),
)
