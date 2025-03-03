import requests
from django.shortcuts import render
from .forms import CityForm  # Make sure this matches

def get_weather_data(city_name):
    api_key = 'dce2aeafae947e1394dab53f13260b03'  # REPLACE THIS
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def home(request):
    weather_data = None
    error_message = None
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city_name']
            try:
                data = get_weather_data(city_name)
                if data['cod'] != 200:
                    error_message = data['message']
                else:
                    weather_data = {
                        'city': data['name'],
                        'temperature': data['main']['temp'],
                        'description': data['weather'][0]['description'],
                        'icon': data['weather'][0]['icon'],
                        'humidity': data['main']['humidity'],
                        'wind_speed': data['wind']['speed'],
                        'country': data['sys']['country']
                    }
            except Exception as e:
                error_message = "Error fetching weather data"
    else:
        form = CityForm()

    return render(request, 'weather_app/home.html', {
        'form': form,
        'weather_data': weather_data,
        'error_message': error_message
    })