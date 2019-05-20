from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from django.utils import timezone

def home(request):
    games = Game.objects
    return render(request, 'game/home.html', {'games':games})

def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    current_move = 1
    return render(request,'game/detail.html', {'game':game})

def create(request):
    if request.method == 'POST':
        if request.POST['phrase']:
            game = Game()
            game.creation_date = timezone.datetime.now()
            game.phrase01 = request.POST['phrase']
            game.save()
            return redirect('/game/' + str(game.id))

def savemove(request):
    if request.method == 'POST':
        game = get_object_or_404(Game, pk=request.POST['game_id'])
        if game.phrase03: # if the game already has last phrase, it is the last move
            if request.FILES['image']:
                game.image03 = request.FILE['image']
                game.save()
        else:
            if game.phrase03: # if the game already has last phrase, it is the last move
                if request.POST['phrase']:
                    game.phrase02 = POST['phrase']
                    game.save()

        return redirect('/game/' + str(game.id))
