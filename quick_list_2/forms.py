from django.forms import ModelForm, TextInput
from quick_list import models

# class GroceryListTestForm(ModelForm):

#     class Meta:
#         model = models.GroceryListTest
#         widgets = {
#             'title': TextInput(attrs={'placeholder': 'What would you like to name your list?'})
#         }

class QuickListForm(ModelForm):

    class Meta:
        model = models.QuickList
        widgets = {
            'title': TextInput(attrs={'placeholder': 'What would you like to name your list?'})
        }


class QuickItemForm(ModelForm):

    class Meta:
        model = models.QuickItem
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Add List Item'})
        }
