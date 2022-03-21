from platform import mac_ver
from django import forms

class User_form(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30) 
    email = forms.EmailField()

class User_found(forms.Form):
    partial_user = forms.CharField(label='Buscador',max_length=20)


