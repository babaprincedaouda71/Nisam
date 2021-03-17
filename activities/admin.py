from django.contrib import admin
from .models import Activitie

class ActivitieAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)

admin.site.register(Activitie, ActivitieAdmin)
