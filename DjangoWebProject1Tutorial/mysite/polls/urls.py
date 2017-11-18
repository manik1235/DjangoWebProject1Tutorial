from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name ='index'),
    url(r'^subpage/$', views.subpage, name ='subpage'),
    url(r'^ruff/$', views.dogpage, name ='dogpage')
]
