from django.contrib import admin

# Register your models here.
from .models import UserProfile, ProfileLink

admin.site.register(UserProfile)
admin.site.register(ProfileLink)
