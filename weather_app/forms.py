from django import forms

class CityForm(forms.Form):
    city_name = forms.CharField(label='Enter City', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter city name...'
    }))