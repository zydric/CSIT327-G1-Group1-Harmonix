from django.urls import path
from . import views
from .views import register, login_view

# urlpatterns = [
#     path('register/', views.register, name='register'),
#     path('login/', views.login, name='login'),
# ]

urlpatterns = [
    path('register/', register),
    path('login/', login_view),
]