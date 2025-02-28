from django import forms
from .models import CarParts

class CarPartsForm(forms.ModelForm):
    class Meta:
        model = CarParts
        fields = ['itemId', 'itemName', 'itemType', 'itemDescription', 'itemPrice', 'itemImage']
