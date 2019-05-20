from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from django.utils import timezone

def home(request):
    return render(request,'game/home.html')

def detail(request, game_id):
    product = get_object_or_404(Game, pk=game_id)
    return render(request,'game/detail.html', {'game':game})


