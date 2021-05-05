from django.contrib import admin
from .models import Post, Comment
from . import models

#class AuthorAdmin(admin.ModelAdmin):
    #list_display = ('title', 'author')

class CommentInline(admin.TabularInline):
    model = Comment
    

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status')
    inlines =[
        CommentInline,
    ]
    
# Register your models here.
admin.site.register(Post, PostAdmin)#AuthorAdmin)
admin.site.register(Comment)