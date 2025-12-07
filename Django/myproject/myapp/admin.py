# myapp/admin.py
from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Customize Post admin interface."""
    list_display = ['title', 'author', 'created_at', 'is_published', 'views']
    list_filter = ['is_published', 'created_at']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at', 'updated_at', 'views']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'author', 'content')
        }),
        ('Status', {
            'fields': ('is_published', 'views')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_at']
    list_filter = ['created_at']
    search_fields = ['author', 'content']
    readonly_fields = ['created_at']
