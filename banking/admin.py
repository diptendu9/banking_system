from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Accholder)
admin.site.register(models.Transactions)
# admin.site.register(models.Transfers)