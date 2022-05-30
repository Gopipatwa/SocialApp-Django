from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.
@admin.register(Users)
class AuthUser(UserAdmin):
    list_display = ['username','first_name','last_name','password','email']

@admin.register(Post)
class UserPost(admin.ModelAdmin):
    list_display = ['userid','img_post']