from django.contrib import admin

from .models import Stream


class StreamAdmin(admin.ModelAdmin):
    list_filter = ['creation_date']
    search_fields = ['stream_name', 'slug']
    list_display = ('stream_name', 'slug', 'creation_date')
    readonly_fields = ('creation_date',)

admin.site.register(Stream, StreamAdmin)
