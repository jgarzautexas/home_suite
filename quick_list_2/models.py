import datetime
from django.db import models

# Create your models here.
class QuickCategory(models.Model):
    name = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=datetime.datetime.now)

    def __unicode__(self):
        return u'{0}'.format(self.name)
    

class QuickList(models.Model):
    title = models.CharField(max_length=30)
    created_date = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now)
    completed = models.BooleanField(default=False)

    def __unicode__(self):
        return u'{0}'.format(self.title)


class QuickItem(models.Model):
    name = models.CharField(max_length=30)
    active = models.BooleanField(default=True)
    quick_list = models.ForeignKey(QuickList, blank=True, null=True)
    category = models.ForeignKey(QuickCategory, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=datetime.datetime.now)


    def __unicode__(self):
        return u'{0}'.format(self.name)