from django.contrib import admin
from .models import User, Profile, Post, Hood, EmergencyService

admin.site.register(User)
admin.site.register(Hood)
admin.site.register(EmergencyService)
