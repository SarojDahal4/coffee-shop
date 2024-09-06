# forms.py
from django import forms
from django.forms import ModelForm
from .models import reservation, contact

class ReservationForm(ModelForm):
    class Meta:
        model = reservation
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'number':forms.TextInput(attrs={'class':'form-control'}),
            'E_mail':forms.TextInput(attrs={'class':'form-control'}),
            'Description':forms.TextInput(attrs={'class':'form-control'}),
            'Quantity':forms.TextInput(attrs={'class':'form-control'}),
            'Event_date':forms.TextInput(attrs={'class':'form-control'}),
            'Event_time':forms.TextInput(attrs={'class':'form-control'})
        }
       
class contactform(ModelForm):
     class Meta:
        model = contact
        fields = "__all__"
        widgets = {
            'Name': forms.TextInput(attrs={'class':'form-control'}),
            'E_mail':forms.TextInput(attrs={'class':'form-control'}), 
            'Number':forms.TextInput(attrs={'class':'form-control'}),
            'Description':forms.TextInput(attrs={'class':'form-control'})
        }