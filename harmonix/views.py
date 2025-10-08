from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing.html')

def home_view(request):
    return render(request, 'home.html')