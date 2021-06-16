from django.contrib import admin
from . models import *

# Register your models here.



class SettingAdmin(admin.ModelAdmin):
    list_display = ('id','title','keywords','company','status','icon','logo','menu_icon','cart_icon')
    list_display_link = ['id','title','company']


class BrandAdmin(admin.ModelAdmin):
    list_display = ['id','title','brands']

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id','name','comment','testimos')

class ContactMessageAdmin(admin.ModelAdmin):
    list_dipslay = ('id','name','email','subject','message','status','note','created_at')
    readonly_fields = ('subject','email','message')
    list_filter = ['status']
    # list_display_links = ('status',)
    search_field = ('name','email','subject','message','status','note')
    list_per_page = 20






admin.site.register(Setting,SettingAdmin)
admin.site.register(Brand,BrandAdmin)
admin.site.register(Testimonial,TestimonialAdmin)
admin.site.register(ContactMessage,ContactMessageAdmin)