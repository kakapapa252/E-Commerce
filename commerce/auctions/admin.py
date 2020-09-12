from django.contrib import admin
from .models import User, Listing, Wishlist

from django.db import models
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	fields = ['username', 'email', 'password',]

admin.site.register(User, UserAdmin)
		
admin.site.register(Listing)

admin.site.register(Wishlist)