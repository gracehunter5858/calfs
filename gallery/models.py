from django.db import models

class Photo(models.Model):
    image_file = models.ImageField(upload_to = '', null = True, blank = True)
    caption = models.CharField(max_length = 200, blank = True, default = '')
    show_in_gallery = models.BooleanField(default = True)
