from django.shortcuts import render
import requests

# Create your views here.
def index(request):
	ow_key = "39a0b9b82fed0bd13d95774fb4374965"
	city = "Minsk"
	url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=" + ow_key

	
	resp = requests.get(url.format(city))

	print(resp.text)

	return render(request, "main/index.html")
