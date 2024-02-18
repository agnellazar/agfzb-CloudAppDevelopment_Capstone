from django.contrib import admin

from djangoapp.models import CarModel, CarMake
# from .models import related models


# Register your models here.
admin.site.register(CarMake)
admin.site.register(CarModel)

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel 
    extra = 5
# CarModelAdmin class

class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'deaelrID', 'type', 'year']
    inlines = [CarModelInline]
# CarMakeAdmin class with CarModelInline

# Register models here
