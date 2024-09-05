import csv
import os
from django.shortcuts import render
from django.http import JsonResponse
import requests


def load_zone_mapping():
    # Initialize an empty dictionary to store the zone mapping
    zone_mapping = {}
    
    # Define the path to the CSV file
    csv_file_path = os.path.join(os.path.dirname(__file__), 'data', 'link.csv')
    
    # Open the CSV file
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        # Create a CSV reader object
        reader = csv.DictReader(csvfile)
        
        # Iterate over each row in the CSV file
        for row in reader:
            # Extract the 'kod_kawasan' and 'nama_kawasan' columns
            kod_kawasan = row['kod_kawasan']
            nama_kawasan = row['nama_kawasan'].strip()
            
            # Add the extracted data to the dictionary
            zone_mapping[kod_kawasan] = nama_kawasan
    
    # Return the populated dictionary
    return zone_mapping

# Create your views here.
def waktusolat_page(request):
    zoneMapping = load_zone_mapping()
    return render(request, "waktusolat.html", {'zoneMapping': zoneMapping})


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

