from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'telefono', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Tu Nombre', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Tu Email', 'required': True}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Tu Teléfono'}),
            'mensaje': forms.Textarea(attrs={'placeholder': 'Tu Mensaje', 'required': True}),
        }