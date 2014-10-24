# from tastypie import fields
# from tastypie.authentication import Authentication
# from tastypie.authorization import Authorization
# from tastypie.validation import Validation, FormValidation
# from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
# from . import models, forms


# class QuickListResource(ModelResource):

#     class Meta:
#         queryset = models.QuickList.objects.all().select_related('grocery_item')
#         resource_name = 'quick_list'
#         authorization = Authorization()
#         authentication = Authentication()
#         validation = FormValidation(form_class=forms.QuickListForm)
#         always_return_data = True
#         allowed_methods = ['get',]


# class QuickItemResource(ModelResource):
#     grocery_list = fields.ForeignKey(QuickListResource, 'grocery_list')
#     # grocery_cat = fields.ForeignKey(GroceryListResource, 'grocery_list')

#     class Meta:
#         queryset = models.QuickListItem.objects.all().select_related('grocery_list__title')
#         resource_name = 'item'
#         authorization = Authorization()
#         validation = FormValidation(form_class=forms.QuickListItemForm)
#         filtering = {
#             'grocery_list': ALL_WITH_RELATIONS,
#         }


'''

     <th>Exception Value:</th>
      <td><pre>You called this URL via POST, but the URL doesn&#39;t

       end in a slash and you have APPEND_SLASH set. Django can&#39;t redirect 



       to the slash URL while maintaining POST data. Change your form to
        point to localhost:8000/api/v1/grocery_list/ (note the trailing slash), or set APPEND_SLASH=False in your Django settings.</pre></td>
      '''