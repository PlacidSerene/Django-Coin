from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests

def index(request):
    response = requests.get('https://api.coingecko.com/api/v3/ping')
    data = response.json()
    print(data)
    return render(request, 'coins/home.html', {
        'status': data['gecko_says']
    })