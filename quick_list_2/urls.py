from django.conf.urls import patterns, include, url
from quick_list_2 import views

urlpatterns = patterns('',
    # url(r'^$', views.index, name='quick_index'),
    
    # url(r'^/(?P<list_id>[0-9]{1,5})/item$', views.quick_list_items, name='quick_list_items'),
    url(r'^$', views.quick_list, name='quick_list'),
    url(r'^/(?P<list_id>[0-9]{1,5})$', views.quick_list_items, name='quick_list_items'),
    
)
