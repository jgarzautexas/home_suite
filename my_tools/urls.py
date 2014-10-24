
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#from quick_list import api, views
from quick_list import views



urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^quick_list', include('quick_list.urls'), name='quick'),
    url(r'^quick_list_2', include('quick_list_2.urls'), name='quick_2'),
    # url(r'^grocery_list', include('grocery_list.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
