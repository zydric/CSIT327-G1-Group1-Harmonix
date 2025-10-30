from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing.html')

@login_required(login_url='login') #added for login required
def home_view(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def listings_view(request):
    """Temporary listings view - will be moved to dedicated listings app later"""
    return render(request, 'listings.html')
