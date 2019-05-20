from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from django.utils import timezone

def home(request):
    games = Game.objects
    return render(request, 'game/home.html', {'games':games}) #

def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if game.image01 is None:
        game.image01 = ""
    return render(request,'game/detail.html', {'game':game})

def create(request):
    if request.method == 'POST':
        if request.POST['phrase']:
            game = Game()
            game.creation_date = timezone.datetime.now()
            game.phrase01 = request.POST['phrase']
            game.save()
            return redirect('/game/' + str(game.id))

def saveimagemove(request, game_id):
    if request.method == 'POST':
        if request.FILES['image']:
            game = get_object_or_404(Game, pk=game_id)
            game.image01 = request.FILE['image']
            game.save()
            return redirect('/game/' + str(game.id))
