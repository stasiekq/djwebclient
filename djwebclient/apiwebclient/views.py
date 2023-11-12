from django.shortcuts import render, redirect
from .forms import HotelBookingForm
import requests
import certifi
from .forms import GetDeleteForm
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
API_URL = "https://localhost:7040/api/HotelBooking/"
#python manage.py runserver

def index(request):
    return render(request, 'apiwebclient/index.html')

def create_update(request):
    if request.method == 'POST':
        form = HotelBookingForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            method = 'POST' if not data['id'] else 'PUT'

            certifi_path = certifi.where()

            response = requests.request(method, f"{API_URL}CreateEdit", json=data, verify = False)
            if response.status_code == 200:
                return redirect('index')
    else:
        form = HotelBookingForm()

    return render(request, 'apiwebclient/create_update.html', {'form': form})

def get(request):
    if request.method == 'POST':
        form = GetDeleteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            response = requests.get(f'https://localhost:7040/api/HotelBooking/Get?id={data["id"]}', verify=False)

            if response.status_code == 200:
                data = response.json()
                return render(request, 'apiwebclient/get.html', {'data': data, 'form': form})
            else:
                return render(request, 'apiwebclient/get.html', {'error_message': f"Error: {response.status_code}", 'form': form})
    else:
        form = GetDeleteForm()

    return render(request, 'apiwebclient/get.html', {'form': form})

def delete(request):
    if request.method == 'POST':
        form = HotelBookingForm(request.POST)
        if form.is_valid():
            guest_id = form.cleaned_data['id']

            certifi_path = certifi.where()

            response = requests.delete(f"{API_URL}Delete?id={guest_id}", verify = False)
            if response.status_code == 204:
                return redirect('index')

    form = HotelBookingForm()
    return render(request, 'apiwebclient/delete.html', {'form': form})

def get_all(request):

    certifi_path = certifi.where()
    response = requests.get(f"{API_URL}GetAll", verify = False)

    if response.status_code == 200:
        data = response.json()
        return render(request, 'apiwebclient/get_all.html', {'data': data})
