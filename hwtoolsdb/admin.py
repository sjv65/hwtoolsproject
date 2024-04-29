from django.contrib import admin
from .models import Tool

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'uses', 'characters']
    list_editable = ['price']
