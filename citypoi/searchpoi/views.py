from django.shortcuts import render

# Create your views here.
def searchpoi_page(request):
    return render(request, 'searchpoi.html')