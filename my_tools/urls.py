
from django.conf.urls import patterns, include, url
# from tastypie.api import Api

from django.contrib import admin
admin.autodiscover()

#from quick_list import api, views
from quick_list import views

# v1_api = Api(api_name='v1')
# v1_api.register(api.GroceryListResource())
# v1_api.register(api.GroceryItemResource())
# grocery_resource = api.GroceryResource()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^quick_list', include('quick_list.urls'), name='quick'),
    url(r'^quick_list_2', include('quick_list_2.urls'), name='quick_2'),
    # url(r'^grocery_list', include('grocery_list.urls')),
    # url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
