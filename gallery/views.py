from django.shortcuts import render
from .models import Photo

# Create your views here.

def gallery(request):
    photos = list(Photo.objects.filter(show_in_gallery = True));
    context = {"photos": photos}
    return render(request, 'gallery/gallery.html', context)
