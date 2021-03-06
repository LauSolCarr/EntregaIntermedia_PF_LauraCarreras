from platform import mac_ver
from django import forms

class User_form(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30) 
    email = forms.EmailField()

class Post_form(forms.Form):
    title = forms.CharField(max_length=20)
    content = forms.CharField(max_length=1000)

class Comment_form(forms.Form):
    content = forms.CharField(max_length=1000)

class User_found(forms.Form):
    partial_user = forms.CharField(label='Buscador',max_length=20)


