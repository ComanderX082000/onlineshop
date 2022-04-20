from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ["title","price","description","rating"]
    list_display_links =["title","price"] 
    search_fields = ["price","title","rating"]

   

class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",)}



admin.site.register(Product,ProductAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(ProductColor)
admin.site.register(Productsize)