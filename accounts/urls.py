from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  
    path('logout/', views.logout_view, name='logout'),

    #Profile & Edit Profile Urls
    #path('profile/', views.get_profile, name='get_profile'),
    # path('profile/edit/', views.edit_profile, name='edit_profile'),

    path('edit_profile/', views.edit_profile, name='edit_profile'),
]