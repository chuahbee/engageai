from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'source', 'tag', 'created_at')
    search_fields = ('name', 'email', 'tag', 'source')
