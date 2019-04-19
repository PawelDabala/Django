from django.contrib import admin

# Register your models here.

from .models import Car, Client, Rent

admin.site.register(Car)
admin.site.register(Client)
admin.site.register(Rent)
