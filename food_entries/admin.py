from django.contrib import admin
from .models import Entry
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Entry)
class EntryAdmin(SummernoteModelAdmin):

    list_filter = ('status', 'created_on')
    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'description']
    summernote_fields = ('description')
    actions = ['approve_entries']

    def approve_entries(self, request, queryset):
        queryset.update(approved=True)
