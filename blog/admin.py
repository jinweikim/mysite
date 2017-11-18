from django.contrib import admin
from django.db import models
from django import forms
from .models import Comment,Image,Article,Category,NewUser,Author,Tag,Train
from .forms import ArticleForm
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_id','article_id','pub_date','content')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name','image')

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    list_display = ('title','pub_date')

class NewUserAdmin(admin.ModelAdmin):
    list_display = ('username','date_joined','profile')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','intro')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','profile')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name','created_time','update_time')

class TrainAdmin(admin.ModelAdmin):
    list_display = ('train_id','start','dest','date','time')

admin.site.register(Comment,CommentAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(NewUser,NewUserAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Train,TrainAdmin)