from django.shortcuts import render, redirect, get_object_or_404
from .models import POI
from .forms import POIForm
from django.core import serializers
import json

def poi_map(request):
    pois = POI.objects.all()
    if pois.exists():
        pois_json = serializers.serialize('json', pois)
    else:
        pois_json = json.dumps([])  # Empty list in JSON format
    return render(request, 'poi/map.html', {'pois_json': pois_json, 'pois': pois})

def add_poi(request):
    if request.method == 'POST':
        form = POIForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('poi_page')
    else:
        form = POIForm()
    return render(request, 'poi/add_poi.html', {'form': form})

def edit_poi(request, pk):
    poi = get_object_or_404(POI, pk=pk)
    if request.method == 'POST':
        form = POIForm(request.POST, instance=poi)
        if form.is_valid():
            form.save()
            return redirect('poi_page')
    else:
        form = POIForm(instance=poi)
    return render(request, 'poi/edit_poi.html', {'form': form})


def delete_poi(request, pk):
    poi = get_object_or_404(POI, pk=pk)
    if request.method == 'POST':
        poi.delete()
        return redirect('poi_page')
    return redirect('poi_page')