from django import forms
from .models import NationalPark,Trail

class NationalParkForm(forms.ModelForm):
    class Meta:
        model = NationalPark
        fields = ['name', 'state', 'picture', 'established']


class TrailForm(forms.ModelForm):
    class Meta:
        model = Trail
        fields = ['name', 'distance', 'elevation', 'difficultyType', 'nationalPark']
        widgets = {
            'difficultyType': forms.Select(),
            'nationalPark': forms.Select(),
        }