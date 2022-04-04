from django.contrib import admin
from engine.models import Car
# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id',"object_id","maker","model","year","category"]

