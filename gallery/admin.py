from django.contrib import admin

# Register your models here.

from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    fields = (
        'image_file', 'show_in_gallery',
    )

admin.site.register(Photo, PhotoAdmin)
