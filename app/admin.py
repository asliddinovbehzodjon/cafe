from django.contrib import admin

# Register your models here.
from .models import Category, Order,Products
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display=('title','category','cost')
    search_fields=('title','desc','cost','category')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('user',)
    search_fields=('title',)
   