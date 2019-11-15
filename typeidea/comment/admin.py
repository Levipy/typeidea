from django.contrib import admin
from .models import Comment
# Register your models here.
from custom_site import custom_site
@admin.register(Comment,site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['target','content','nickname','website','created_time']
