from django import forms
from .models import *

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptops
        fields = ('type', 'price', 'quantity','supplier', 'date')


class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktops
        fields = ('type', 'price', 'quantity','supplier', 'date')
        

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobiles
        fields = ('type', 'price', 'quantity','supplier', 'date')
