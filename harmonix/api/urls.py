from django.urls import path
from . import views

urlpatterns = [
    # User authentication endpoints
    path('register/', views.RegisterView.as_view(), name='api-register'),
    path('login/', views.LoginView.as_view(), name='api-login'),
    path('logout/', views.LogoutView.as_view(), name='api-logout'),

    # Profiles
    path('musician/<int:pk>/', views.MusicianProfileView.as_view(), name='api-musician-profile'),
    path('band/<int:pk>/', views.BandProfileView.as_view(), name='api-band-profile'),

    # Listings
    path('listings/', views.ListingListCreateView.as_view(), name='api-listings'),
    path('listings/<int:pk>/', views.ListingDetailView.as_view(), name='api-listing-detail'),
]
