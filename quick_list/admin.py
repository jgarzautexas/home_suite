from django.contrib import admin
from . import models
# Register your models here.

class QuickListItemInline(admin.TabularInline):
    model = models.QuickListItem


class QuickListAdmin(admin.ModelAdmin):
    inlines = [QuickListItemInline]

class GroceryListTestAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.QuickList, QuickListAdmin)
admin.site.register(models.QuickListCategory)
admin.site.register(models.QuickListItem)

