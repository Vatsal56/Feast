from django.contrib import admin
from restaurant.models import food_item, drink_item, table,Order
# Register your models here.

admin.site.register(food_item)
admin.site.register(drink_item)
admin.site.register(table)
admin.site.register(Order)
