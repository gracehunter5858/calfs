from django.shortcuts import render
from .models import Photo

# Create your views here.

def gallery(request):
    context = {}
    photos = list(Photo.objects.filter(show_in_gallery = True));
    if photos:
        context = {'first_photo': photos[0], 'rest_of_photos': photos[1:]}
    else:
        context = {'first_photo': [], 'rest_of_photos': []}
    return render(request, 'gallery/gallery.html', context)
