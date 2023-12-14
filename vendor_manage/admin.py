from django.contrib import admin
from .models import Vendor,Purchase,HistoricalPerformance
# Register your models here.

admin.site.register(Vendor)
admin.site.register(Purchase)
admin.site.register(HistoricalPerformance)