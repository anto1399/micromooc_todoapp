# Import required packages amd modules
from django.contrib import admin
from .models import Todo


# Make Todos Available to Admin Dashboard and customize how it appears on the dashboard
@admin.register(Todo)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'creator')
    search_fields = ('title', 'description')
    raw_id_fields = ('creator',)
    date_hierarchy = 'created_at'

