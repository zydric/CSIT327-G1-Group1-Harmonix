from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Application
from listings.models import Listing


@login_required
def apply_to_listing(request, listing_id):
    """
    Handle musician applications to band listings
    """
    listing = get_object_or_404(Listing, id=listing_id, is_active=True)
    
    # Only musicians can apply
    if not request.user.is_musician:
        messages.error(request, "Only musicians can apply to listings.")
        return redirect('listings:feed')
    
    # Check if already applied
    if listing.is_applied_by(request.user):
        messages.warning(request, "You have already applied to this listing.")
        return redirect('listings:feed')
    
    if request.method == 'POST':
        message = request.POST.get('message', '')
        
        # Create the application
        Application.objects.create(
            musician=request.user,
            listing=listing,
            message=message
        )
        
        messages.success(request, f"Your application to '{listing.title}' has been submitted!")
        return redirect('listings:feed')
    
    # GET request - show application form
    context = {
        'listing': listing,
    }
    return render(request, 'applications/apply.html', context)


@login_required 
def my_applications(request):
    """
    Show musician's applications or band admin's received applications
    """
    if request.user.is_musician:
        # Show applications made by this musician
        applications = Application.objects.filter(musician=request.user)
        template = 'applications/my_applications.html'
    else:
        # Show applications to this band's listings
        applications = Application.objects.filter(listing__band_admin=request.user)
        template = 'applications/received_applications.html'
    
    context = {
        'applications': applications,
    }
    return render(request, template, context)