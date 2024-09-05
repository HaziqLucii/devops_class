from django.urls import path
from . import views

urlpatterns = [
    path('', views.poi_map, name='poi_page'),
    path('add/', views.add_poi, name='add_poi'),
    path('edit/<int:pk>/', views.edit_poi, name='edit_poi'),
]

