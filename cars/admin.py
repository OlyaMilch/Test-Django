from django.contrib import admin
from .models import Car, Manufacturer, Country, Comment


admin.site.register(Car)
admin.site.register(Manufacturer)
admin.site.register(Country)
admin.site.register(Comment)
