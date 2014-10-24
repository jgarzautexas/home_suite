import datetime
from django.db import models


class QuickListCategory(models.Model):
    category = models.CharField(max_length=30)

    def __unicode__(self):
        return u'{0}'.format(self.category)
    

class QuickList(models.Model):
    title = models.CharField(max_length=30)
    created_date = models.DateTimeField(
        null=True,
        blank=True,
        default=datetime.datetime.now
        )
    completed = models.BooleanField(default=False)

    def __unicode__(self):
        return u'{0}'.format(self.title)


class QuickListItem(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    quick_list = models.ForeignKey(QuickList, blank=True, null=True)
    category = models.ForeignKey(QuickListCategory, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=datetime.datetime.now)


    def __unicode__(self):
        return u'{0}'.format(self.name)

    # class Meta:
    #     unique_together = (("item", "grocery_list"),)

# class GroceryListTest(models.Model):
#     title = models.CharField(max_length=30)
#     created_date = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now)
#     completed = models.BooleanField(default=False)
#     items = models.ManyToManyField(GroceryItem)

#     def __unicode__(self):
#         return u'{0}'.format(self.title)
