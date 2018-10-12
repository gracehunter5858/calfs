from django.db import models
from django.conf import settings

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length = 30)
    year_choices = (
        (1, 'Freshman'),
        (2, 'Sophomore'),
        (3, 'Junior'),
        (4, 'Senior'),
        (5, 'Graduate')
    )
    year = models.IntegerField(choices = year_choices, default = 1)
    major_1 = models.CharField(max_length = 50, blank = True, default = '')
    major_2 = models.CharField(max_length = 50, blank = True, default = '')
    minor_1 = models.CharField(max_length = 50, blank = True, default = '')
    minor_2 = models.CharField(max_length = 50, blank = True, default = '')
    hometown = models.CharField(max_length = 50, blank = True, default = '')
    photo = models.ImageField(upload_to = '', null = True, blank = True)
    officer_choices = (
        (1, 'President'),
        (2, 'Vice President'),
        (3, 'Team Captain'),
        (4, 'Treasurer'),
        (5, 'PR Chair'),
        (6, 'Fundraising Chair'),
        (7, 'Social/Rec Chair')
    )
    officer_position = models.IntegerField(choices = officer_choices, null = True, blank = True)

    def __str__(self):
        return self.name

    def photo_uploaded(self):
        return self.photo != None
    photo_uploaded.boolean = True


    # These two auto-delete files from filesystem when they are unneeded:
