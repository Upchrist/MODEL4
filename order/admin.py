from django.contrib import admin
from django.db.models import fields
from .models import *

# Register your models here.

class ShopCartAdmin(admin.ModelAdmin):
    list_display=('order_code','user','product','quantity','size','price','amount','order_placed')
    list_filter=['user']
    list_display_links = ['product']
    readonly_fields = ('order_code','user','product','quantity','size','price','amount','order_placed')
    can_delete = False



class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_code','user','order_placed','payment_code', 'total','status','created_at')
    list_filter = ['status']
    list_display_link = ('order_code','user','order_placed','payment_code','total','status','created_at')
    can_delete = False

admin.site.register(Order, OrderAdmin)
admin.site.register(ShopCart, ShopCartAdmin)
