from django.contrib import admin
from . models import Product, JamesDick, Discount

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock') 


class JamesDickAdmin(admin.ModelAdmin):
    list_display = ('Length', 'Girth') 


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_num') 



admin.site.register(Discount, DiscountAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(JamesDick, JamesDickAdmin)
