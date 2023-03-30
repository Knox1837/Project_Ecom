from django.contrib import admin
from .models import Product, Category


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=('category_name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "desc", "category", "price", "quantity", "discount", "cash_on_delivery")
    search_fields=('title', 'category')
    list_filter=('title', 'category', 'user')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


#Admin panel customization
admin.site.site_title='ADMIN'
admin.site.site_header="Ecom Project"
admin.site.index_title="Ecom"