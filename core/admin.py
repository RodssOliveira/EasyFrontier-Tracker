__author__ = 'Rodrigo.Oliveira'

from django.contrib import admin
from core.models import Tracker

@admin.register(Tracker)
class Tracker(admin.ModelAdmin):
    list_display = ['id', 'name', 'patent']
    search_fields = ['id', 'name', 'patent']

