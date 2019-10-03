from django.contrib import admin

# Register your models here.
from .models import Order, Product, SubT, PizzaT

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(SubT)
admin.site.register(PizzaT)