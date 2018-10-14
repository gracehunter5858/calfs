from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def join(request):
    return render(request, 'join.html', {})

def about(request):
    return render(request, 'about.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, 'ucbfigureskating@gmail.com', ['ucbfigureskating@gmail.com'])
            return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
