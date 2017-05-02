from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^destination/(?P<id>\d+)$',views.destination, name='destination'),
    url(r'^add$',views.add, name='add'),
    url(r'^join/(?P<id>\d+)$',views.join, name='join'),
    url(r'^create$',views.create, name='create'),
    # url(r'^combine$',views.combine, name='combine'),


]