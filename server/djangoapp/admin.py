from django.contrib import admin
from .models import CarModel, CarMake


# TO DO: Register your models here. Afterward, you will see your models appearing on localhost:8080/admin
admin.site.register(CarMake)
admin.site.register(CarModel)
# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
