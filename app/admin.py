from django.contrib import admin

# Register your models here.
from .models import Category,Products
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display=('title','category','cost')
    search_fields=('title','desc','cost','category')
   