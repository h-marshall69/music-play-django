from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .forms import CustomUserCreationForms, MusicForm
from .models import Music

# Create your views here.


def home(request):
    return render(request, 'home.html')

@login_required
def media(request):
    return render(request, 'media.html')

def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    data = {
        'form': CustomUserCreationForms()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForms(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    return render(request, 'registration/register.html', data)


def upload_music(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            music = form.save(commit=False)
            music.user = request.user
            music.save()
            return redirect('home')  # Redirige a la página de lista de música
    else:
        form = MusicForm()
    return render(request, 'upload_music.html', {'form': form})

def music_list(request):
    songs = Music.objects.all()
    return render(request, 'music_list.html', {'songs': songs})