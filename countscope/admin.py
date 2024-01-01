from django.contrib import admin
from .models import CountScope

@admin.register(CountScope)
class CountScopeAdmin(admin.ModelAdmin):
    list_display=("title","isActive","slug",)
    list_display_links=("title","slug",)
    list_filter=("isActive",)
    list_editable=("isActive",)
    search_fields=("title","description")

