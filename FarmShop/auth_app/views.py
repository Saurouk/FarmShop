from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ContactForm


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Votre compte a été créé avec succès ! Bienvenue {username}')
            return redirect('home')  # Redirige vers la page d'accueil après l'inscription
    else:
        form = UserRegisterForm()

    # Corriger le chemin ici
    return render(request, 'register/register.html', {'form': form})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Ajout du traitement
            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
