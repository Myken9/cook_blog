from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "create_at", "id"]


@admin.register(models.Reciept)
class Reciept(admin.ModelAdmin):
    list_display = ["name", "prep_time", "cook_time", "post"]


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Comment)
admin.site.register(models.Tag)
