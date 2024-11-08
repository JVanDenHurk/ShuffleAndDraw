from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Card

class CardAdmin(ModelAdmin):
    list_display = ['name', 'description', 'stock', 'image']
    search_fields = ['name', 'description']
    list_filter = ['name']

admin.site.register(Card, CardAdmin)
