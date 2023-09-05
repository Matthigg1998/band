from django.shortcuts import render, get_object_or_404, redirect
from .models import Band, Song
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

@login_required
def home(request):
    # Assuming you want to link to the first band in your database
    band = Band.objects.first()
    return render(request, 'band/home.html', {'band': band})

@login_required
def band_info(request, band_id):
    band = get_object_or_404(Band, pk=band_id)
    return render(request, 'band/band_info.html', {'band': band})

@login_required
def song_list(request):
    songs = Song.objects.all()
    return render(request, 'band/song_list.html', {'songs': songs})

def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('band:home')  # Redirect to the home page
    else:
        form = UserCreationForm()
        return render(request, 'band/registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('band:home')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'band/login.html')