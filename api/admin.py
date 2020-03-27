from django.contrib import admin
from .models import User, Bussiness, Hood, EmergencyService

admin.site.register(User)
admin.site.register(Hood)
admin.site.register(EmergencyService)
admin.site.register(Bussiness)
