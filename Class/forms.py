from django import forms

class User_form(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30) 
    email = forms.EmailField()


