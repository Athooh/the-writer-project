from django.contrib import admin
from .models import Author

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'job_description', 'is_mvp', 'hire_date')
    list_display_links = ('id', 'name', 'job_description')
    list_filter = ('name',)
    search_fields = ('name', 'hire_date')
    list_per_page = 25
    
admin.site.register(Author, AuthorAdmin)