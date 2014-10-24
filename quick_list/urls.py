from django.conf.urls import patterns, include, url
from quick_list import  views

urlpatterns = patterns('',
    url(r'^$', views.quick_list, name='quick_list'),
    
    url(r'^/(?P<list_id>[0-9]{1,5})/items$', views.quick_list_items, name='grocery_list_items'),
    # url(r'^/(?P<list_id>[0-9]{1,5})$', views.grocery_list, name='grocery_list'),
    
)
