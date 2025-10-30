from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('apply/<int:listing_id>/', views.apply_to_listing, name='apply'),
    path('my-applications/', views.my_applications, name='my_applications'),
]