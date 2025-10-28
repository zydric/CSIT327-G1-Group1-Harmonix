from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  
    path('logout/', views.logout_view, name='logout'),
    path('musician_profile/', views.musician_profile_view, name='musician_profile'),
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
]