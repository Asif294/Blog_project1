from django.contrib import admin
from . import models
admin.site.register(models.post)
admin.site.register(models.comment)
