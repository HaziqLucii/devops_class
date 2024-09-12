import requests
from django.shortcuts import render


def searchpoi_page(request):
    apiUrl = 'https://mymaps.mygeoportal.gov.my/api/datasets/'
    # headers = {'Authorization': 'Bearer MyG3oHub2023SH@PGN'}

    # Fetch layers from API
    response = requests.get(apiUrl)
    layers = response.json().get('objects', [])

    context = {
        'layers': layers,
    }

    return render(request, 'searchpoi.html', context)
