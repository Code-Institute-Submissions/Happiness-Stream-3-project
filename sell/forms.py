from django import forms
from.models import Sell

class SellForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = ('car_name', 'car_model','descriptions','image','price')
        