from django.contrib import admin
from .models import Resource, BlogPost

admin.site.register(Resource)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'topic', 'created_at')