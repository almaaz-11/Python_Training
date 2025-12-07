from django.contrib import admin
from .models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','created_at','is_published','views']

    list_filter = ['is_published','created_at']

    search_fields = ['title', 'content']

    readonly_fields = ['created_at', 'updated_at', 'views']

    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','author','created_at','get_post_title']
    list_filter = ['created_at', 'post']

    search_fields = ['author' , 'content']

    def get_post_title(self, obj):
        return obj.post.title

    get_post_title.short_description = 'Post Title'