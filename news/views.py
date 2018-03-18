from django.shortcuts import render
from .models import Event

# Create your views here.

def index(request):
        events = Event.objects.order_by('start')
        context = {'events': events}
        return render(request, 'news/index.html', context)
