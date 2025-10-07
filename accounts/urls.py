from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # Changed to login_view
    path('logout/', views.logout_view, name='logout'),
    path('', views.home_view, name='home'),  # Dashboard/home
]