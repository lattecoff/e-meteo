from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
	ow_key = open("./ow_key.txt", "r").readline()
	url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + ow_key

	if (request.method == "POST"):
		form = CityForm(request.POST)
		form.save()


	form = CityForm

	cities = City.objects.all()

	list_cities = []

	for city in cities:
		resp = requests.get(url.format(city)).json()
	
		city_info = {
			"city": city,
			"temp": resp["main"]["temp"],
			"icon": resp["weather"][0]["icon"]
		}

		list_cities.append(city_info)


	context = {"all_info": list_cities, "form": form}

	return render(request, "main/index.html", context)
