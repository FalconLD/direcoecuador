# core/forms.py

from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'telefono', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Tu Nombre'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Tu Email'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Tu Teléfono'}),
            'mensaje': forms.Textarea(attrs={'placeholder': 'Tu Mensaje'}),
        }