from django.shortcuts import render
from django.http import JsonResponse
import requests
from datetime import datetime


# Create your views here.
def waktusolat_page(request):
    return render(request, "waktusolat.html")


def reverse_geocode(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')

    url = f'https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json&addressdetails=1'
    response = requests.get(url)
    data = response.json()

    if data and 'address' in data:
        district = data['address'].get('district', 'District not found')
        return JsonResponse({'district': district})
    else:
        return JsonResponse({'error': 'Address not found'}, status=404)

