from django.db import models
from sorl.thumbnail import ImageField
from django.utils.html import mark_safe
from sorl.thumbnail import get_thumbnail

class Photo(models.Model):
    image = ImageField(upload_to = '', null = True, blank = True)
    show_in_gallery = models.BooleanField(default = True)

    def thumb(self):
        if self.image:
            return mark_safe('<img src="%s" />' % (get_thumbnail(self.image, "100x100", crop='center', quality=95).url))

    def __str__(self):
        return self.image.name
