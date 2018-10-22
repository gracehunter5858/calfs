from django.contrib import admin

# Register your models here.

from .models import Photo

class PhotoAdmin(admin.ModelAdmin):

    fields = (
        'image', 'show_in_gallery',
    )

    list_display = (
        'thumb', 'show_in_gallery'
    )
    
admin.site.register(Photo, PhotoAdmin)
