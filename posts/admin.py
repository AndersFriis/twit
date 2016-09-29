from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    
admin.site.register(Post, PostAdmin)




