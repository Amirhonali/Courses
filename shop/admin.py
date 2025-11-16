from django.contrib import admin
from . import models
# Create your views here.

admin.site.register(models.Course)
admin.site.register(models.Category)