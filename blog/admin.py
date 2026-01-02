from django.contrib import admin
from .models import Post

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['pidrozdil', 'marshrut', 'sostav', 
                    'data_viezd', 'time_viezd', 'time_back',
                    'publish', 'status']

    
# Register your models here.
