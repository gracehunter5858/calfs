from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length = 30)
    start = models.DateTimeField()
    end = models.DateTimeField(null = True, blank = True)
    date_display_options = (
        ("single date", "single date"),
        ("date range", "date range")
    )
    time_display_options = (
        ("start time only", "start time only"),
        ("time range", "time range"),
        ("no time", "no time")
    )
    date_display_format = models.CharField(max_length = 20, choices=date_display_options, default = "single date")
    time_display_format = models.CharField(max_length = 20, choices=time_display_options, default = "start time only")
    price = models.DecimalField(max_digits = 5, decimal_places = 2, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    photo = models.ImageField(upload_to = '', null = True, blank = True)
    display_on_site = models.BooleanField(default = True)

    def __str__(self):
        return self.name
