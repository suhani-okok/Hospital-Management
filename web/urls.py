# web/urls.py

from django.urls import path
from .views import index, login, home

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    # Other URL patterns...
]
