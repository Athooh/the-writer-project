from django.contrib import admin
from .models import Brands


# Register your models here.
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('category','author', 'title', 'is_published', 'post_date')
    list_display_links = ('category', 'title', 'author')
    list_filter = ('category','author','is_published')
    search_fields = ( 'author__name', 'title', 'post_date', 'category')
    list_per_page = 25

admin.site.register(Brands, BrandsAdmin)