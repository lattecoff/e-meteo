from django.forms import ModelForm, TextInput, widgets
from .models import City


class CityForm(ModelForm):
	class Meta:
		model = City
		fields = ["name"]
		widgets = {"name": TextInput(attrs={
			"class": "form-control",
			"name": "city",
			"id": "city",
			"placeholder": "Enter city"
			})}


