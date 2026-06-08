# core/views.py

from django.shortcuts import render, redirect
from .forms import ContactoForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gracias por tu mensaje! Nos pondremos en contacto contigo pronto.')
            return redirect('index')
    else:
        form = ContactoForm()

    return render(request, 'core/index.html', {'form': form})