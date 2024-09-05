from django.urls import path
from . import views

urlpatterns = [
    path('', views.waktusolat_page, name='waktusolat_page'),
    path('reverse-geocode/', views.reverse_geocode, name='reverse_geocode'),
]