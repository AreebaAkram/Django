from django.contrib import admin

# Register your models here.
from .import models
admin.site.register(models.task)
admin.site.register(models.date)
