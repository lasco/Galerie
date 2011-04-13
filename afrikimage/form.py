from models import *
from django import forms
from django.forms.widgets import RadioSelect

class SearchForm(forms.Form):
    prenom = forms.CharField(max_length=30)
    nom= forms.CharField(max_length=30)

class PhotoForm(forms.ModelForm):
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
    
    
checkboxchoice1 =  [['I','Interieur'],['E','Exterieur']]
checkboxchoice2 = [['P','Printemps'],['E','Ete'],['A','Automne'],['H','Hiver']]
checkboxchoice3 = [['M','Maison'],['B','Bureau'],['S','Studio'],['A','Autre']]
checkboxchoice4 = [['V','Ville'],['V','Village'],['N','Nature']]

class LieuxForm(forms.Form):
    cadre = forms.ChoiceField(widget=RadioSelect(),choices=checkboxchoice1)
    saison = forms.ChoiceField(widget=RadioSelect(),choices=checkboxchoice2)
    type_in = forms.ChoiceField(label='Type d interieur',widget=RadioSelect(),choices=checkboxchoice3)
    type_ex = forms.ChoiceField(label='Type d exterieur',widget=RadioSelect(),choices=checkboxchoice4)
