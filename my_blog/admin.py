from django.contrib import admin
from .models import Post, Comment
from . import models


class CommentInline(admin.TabularInline):
    model = Comment
    

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status')
    inlines =[
        CommentInline,
    ]
    
# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)