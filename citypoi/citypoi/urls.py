from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('map/', include('waktusolat.urls')),
    path('poi/', include('poi.urls')),
]
