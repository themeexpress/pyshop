from django.contrib import admin
from .models import Products, Offer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')


admin.site.register(Products,ProductAdmin)


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','description','discount')


admin.site.register(Offer,OfferAdmin)


