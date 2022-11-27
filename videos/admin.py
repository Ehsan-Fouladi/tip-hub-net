from django.contrib import admin
from . import models

admin.site.site_header = "کد یاد"



@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("user", 'slug', 'image', 'video', 'time', 'status')
    list_filter = ('slug', 'time', 'status')
    search_fields = ("status",)


admin.site.register(models.Comment)
