from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Listing
from applications.models import Application


@login_required
def listings_view(request):
    """
    Main listings page - shows different content based on user role:
    - Musicians see available opportunities they can apply to
    - Band admins see their own listings and can manage them
    """
    user = request.user
    
    # Get filter parameters
    search_query = request.GET.get('search', '')
    genre_filter = request.GET.get('genre', '')
    instrument_filter = request.GET.get('instrument', '')
    location_filter = request.GET.get('location', '')
    
    if user.is_musician:
        # Musicians see all active listings
        listings = Listing.objects.filter(is_active=True)
        
        # Apply filters
        if search_query:
            listings = listings.filter(
                Q(title__icontains=search_query) |
                Q(band_name__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        
        if genre_filter:
            listings = listings.filter(genres__icontains=genre_filter)
            
        if instrument_filter:
            listings = listings.filter(instruments_needed__icontains=instrument_filter)
            
        if location_filter:
            listings = listings.filter(location__icontains=location_filter)
            
        # Order by newest first
        listings = listings.order_by('-created_at')
        
        # Get unique filter options for dropdowns
        all_listings = Listing.objects.filter(is_active=True)
        
        # Use standardized genre choices
        available_genres = [choice[0] for choice in Listing.GENRE_CHOICES]
        available_instruments = [choice[0] for choice in Listing.INSTRUMENT_CHOICES]
        
        # Get actual genres and instruments from listings
        used_genres = set()
        used_instruments = set()
        locations = set()
        
        for listing in all_listings:
            used_genres.update(listing.genres_list)
            used_instruments.update(listing.instruments_list)
            locations.add(listing.location)
        
        # Filter to only show genres/instruments that are actually used and in our choices
        filter_options = {
            'genres': [g for g in available_genres if g in used_genres],
            'instruments': [i for i in available_instruments if i in used_instruments],
            'locations': sorted([loc for loc in locations if loc])  # Remove empty locations
        }
        
    else:  # Band admin
        # Band admins see only their own listings
        listings = Listing.objects.filter(band_admin=user).order_by('-created_at')
        filter_options = {}  # Band admins don't need filters for their own listings
    
    context = {
        'user': user,
        'listings': listings,
        'listings_count': listings.count(),
        'is_musician': user.is_musician,
        'is_band_admin': user.is_band_admin,
        'filter_options': filter_options,
        'current_filters': {
            'search': search_query,
            'genre': genre_filter,
            'instrument': instrument_filter,
            'location': location_filter,
        }
    }
    
    return render(request, 'listings/listings_feed.html', context)
