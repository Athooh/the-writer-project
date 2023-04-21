from django.contrib import admin
from .models import Post
from .models import Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'post_id', 'title', 'is_published', 'post_date')
    list_display_links = ('post_id', 'title', 'author')
    list_filter = ('author',)
    search_fields = ( 'author__name', 'title', 'post_date')
    list_per_page = 25
     
admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'date_added', 'active')
    list_filter = ('active', 'date_added')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Comment, CommentAdmin)