from django.shortcuts import render
from .models import Member

# Create your views here.

def index(request):
    officers = list(Member.objects.exclude(officer_position = None).order_by('officer_position'))
    non_officers = list(Member.objects.filter(officer_position = None).order_by('-year'))
    members = officers + non_officers
    context = {'members': members}
    return render(request, 'team/index.html', context)
