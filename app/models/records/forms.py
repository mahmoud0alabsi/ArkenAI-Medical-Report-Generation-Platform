from .models import *
from django.contrib import admin, messages

# @admin.register(SavedRecord)
class SavedRecordAdmin(admin.ModelAdmin):

    model = SavedRecord

    list_display = ("id", "user", 'title', 'recorded', 'date_created')
    list_filter = ('user', 'recorded', 'date_created')
    search_fields = ('user', )
    ordering = ('date_created', )


class TempRecordAdmin(admin.ModelAdmin):

    model = TempRecord

    list_display = ("id", "user", 'recorded', 'date_created')
    list_filter = ('user', 'recorded', 'date_created')
    search_fields = ('user', )
    ordering = ('date_created', )
