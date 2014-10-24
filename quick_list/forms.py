
from django.forms import ModelForm, TextInput
from quick_list import models

# class QuickListTestForm(ModelForm):

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


class QuickListItemForm(ModelForm):

    class Meta:
        model = models.QuickListItem
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Add List Item'})
        }

    # def clean_category(self):
    #     print "I need to clean the category"