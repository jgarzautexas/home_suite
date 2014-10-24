from django.contrib import admin
from . import models

class QuickItemInline(admin.TabularInline):
    model = models.QuickItem

class QuickListAdmin(admin.ModelAdmin):
    inlines = [QuickItemInline]

admin.site.register(models.QuickList, QuickListAdmin)
admin.site.register(models.QuickItem)

# Register your models here.
