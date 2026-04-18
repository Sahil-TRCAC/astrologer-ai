# astrologer_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get-astrology-reading/', views.get_astrology_reading, name='get_astrology_reading'),
]