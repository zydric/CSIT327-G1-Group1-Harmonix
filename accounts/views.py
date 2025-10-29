from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

# REST FRAMEWORKS (Imports are not used in these views)
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

from .models import User

# ============================
# Registration View
# ============================
@csrf_protect
def register(request):
    if request.method == 'POST':
        # --- Get form data ---
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        role = request.POST.get('role')

        # --- Validation ---
        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'accounts/register.html')

        if len(password1) < 8:
            messages.error(request, 'Password must be at least 8 characters long!')
            return render(request, 'accounts/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return render(request, 'accounts/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return render(request, 'accounts/register.html')

        if not role or role not in ['musician', 'band']:
            messages.error(request, 'Please select a valid role!')
            return render(request, 'accounts/register.html')

        # --- Create user ---
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                role=role
            )
            messages.success(request, 'Registration successful! Please login.')
            return redirect('login')

        except Exception as e:
            messages.error(request, f'Registration failed: {str(e)}')
            return render(request, 'accounts/register.html')

    # Handle GET request
    return render(request, 'accounts/register.html')


# ============================
# Login View
# ============================
@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login successful
            auth_login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            
            # Redirect to 'next' page or default to 'home_view'
            next_page = request.GET.get('next', 'home_view')
            return redirect(next_page)
        else:
            # Login failed
            messages.error(request, 'Invalid username or password!')

    # Handle GET request
    return render(request, 'accounts/login.html')


# ============================
# Logout View
# ============================
@never_cache  # Prevents caching of the logout page
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')


# ============================
# Profile View
# ============================
@login_required
@csrf_protect
def musician_profile_view(request):
    context = {
        'user': request.user
    }
    return render(request, 'accounts/musician_profile.html', context)


# ============================
# Edit Profile View
# ============================
@login_required
@csrf_protect
def edit_profile_view(request):
    user = request.user
    
    if request.method == 'POST':
        # --- Update user fields from form data ---
        # Use .get(field, default_value) to keep old value if field is not in POST
        user.username = request.POST.get('fullname', user.username)
        user.location = request.POST.get('location', user.location)
        user.genres = request.POST.get('genres', user.genres)
        user.instruments = request.POST.get('instruments', user.instruments)

        try:
            user.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('musician_profile') 
        except Exception as e:
            # Handle potential save errors (e.g., username already taken)
            messages.error(request, f'An error occurred: {e}')
            
    # Handle GET request (or POST failure)
    context = {
        'user': user
    }
    return render(request, 'accounts/edit_musician_profile.html', context)