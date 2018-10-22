from django.db import models
from PIL import Image as Img
from io import BytesIO

class Photo(models.Model):
    image = models.ImageField(upload_to = '', null = True, blank = True)
    caption = models.CharField(max_length = 200, blank = True, default = '')
    show_in_gallery = models.BooleanField(default = True)

    def save(self, *args, **kwargs):
        if self.image:
            img = Img.open(BytesIO(self.image.read()))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.thumbnail((self.image.width/1.5,self.image.height/1.5), Img.ANTIALIAS)
            output = BytesIO()
            img.save(output, format='JPEG', quality=70)
            output.seek(0)
            self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', output.len, None)
        super(Images, self).save(*args, **kwargs)
