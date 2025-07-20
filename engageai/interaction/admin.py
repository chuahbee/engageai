from django.contrib import admin
from .models import InteractionRecord, KMPInteraction
from django.contrib import admin

@admin.register(InteractionRecord)
class InteractionRecordAdmin(admin.ModelAdmin):
    list_display = ('customer', 'channel', 'created_at')
    search_fields = ('customer__name', 'content')
    list_filter = ('channel',)

@admin.register(KMPInteraction)
class KMPInteractionAdmin(admin.ModelAdmin):
    list_display = ('input_text', 'matched_keyword', 'created_at')
    search_fields = ('input_text', 'matched_keyword')