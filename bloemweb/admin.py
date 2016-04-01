from django.contrib import admin

# Register your models here.
from . import models

class FlowerGroupsInLine(admin.TabularInline):
    model = models.FlowerGroup
    extra = 0


admin.site.register(models.FlowerGroup)
