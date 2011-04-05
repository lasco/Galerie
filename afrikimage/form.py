from models import *
from django import forms


class SearchForm(forms.Form):
    prenom = forms.CharField(max_length=30)
    nom= forms.CharField(max_length=30)

class PhotoForm(forms.ModelForm):
    #~ file_ = forms.Field(widget=forms.FileInput, required=False)
    class Meta:
        model = Photo


class Autorform(forms.Form):
    nom = forms.CharField(max_length=30)
    prenom =forms.CharField(max_length=30)
    nationalite=forms.CharField(max_length=30)
    date1= forms.DateField(label='date de naissance')
    adresse =forms.CharField(max_length = 200)
    email = forms.EmailField ()
    experience = forms.IntegerField(required=False)
