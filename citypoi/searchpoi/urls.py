from django.urls import path
from . import views

urlpatterns = [
    path('', views.searchpoi_page, name='searchpoi_page'),
]

