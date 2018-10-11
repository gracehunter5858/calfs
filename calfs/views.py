from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def join(request):
    return render(request, 'join.html', {})

def about(request):
    return render(request, 'about.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def contact(request):
    return render(request, 'contact.html', {})
