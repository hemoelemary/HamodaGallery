from django.contrib import admin
from .models import Post
# Register your models here.

class AdminPost(admin.ModelAdmin):
    pass
admin.site.register(Post,AdminPost)