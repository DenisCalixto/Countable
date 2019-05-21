from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from django.utils import timezone

def home(request):
    games = Game.objects
    return render(request, 'game/home.html', {'games':games})

def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if game.phrase03: # if third phrase exists, this is the sixth move. One to go
        current_move = 'image'
    elif game.image02:  # if second image exists, this is the fifth move. Two to go
        current_move = 'phrase'
    elif game.phrase02: # if second phrase exists, this is the forth move.
        current_move = 'image'
    elif game.image01: # if first image exists, this is the third move.
        current_move = 'phrase'
    else: # this is the second move.
        current_move = 'image'
    return render(request,'game/detail.html', {'game':game,'current_move':current_move})

def create(request):
    if request.method == 'POST':
        if request.POST['phrase']:
            game = Game()
            game.creation_date = timezone.datetime.now()
            game.phrase01 = request.POST['phrase'] # creating the game already with the first move taken
            game.save()
            return redirect('/game/' + str(game.id)) # once created, show game's details

def savemove(request, game_id):
    if request.method == 'POST':
        game = get_object_or_404(Game, pk=game_id)
        if game.phrase03: # if third phrase exists, this is the sixth move. One to go
            game.image03 = request.FILES['image']
            game.save()
        elif game.image02:  # if second image exists, this is the fifth move. Two to go
            game.phrase03 = request.POST['phrase']
            game.save()
        elif game.phrase02: # if second phrase exists, this is the forth move.
            game.image02 = request.FILES['image']
            game.save()
        elif game.image01: # if first image exists, this is the third move.
            game.phrase02 = request.POST['phrase']
            game.save()
        else: # this is the second move.
            game.image01 = request.FILES['image']
            game.save()

        return redirect('/game/' + str(game.id), {'message':'Move saved!'})
