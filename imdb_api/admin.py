from django.contrib import admin
from .models import StreamPlatform, WatchList

# Register your models here
@admin.register(StreamPlatform)
class StreamPlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'about', 'website')


@admin.register(WatchList)
class WatchListAdmin(admin.ModelAdmin):
    list_display = ('title', 'platform', 'active', 'created')
    list_filter = ('active', 'platform')
    search_fields = ('title', 'storyline')
