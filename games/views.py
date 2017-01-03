from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import GameForm
from .models import Game

@login_required
def list_view(request):
   user = request.user
   form = GameForm(request.POST or None)

   if(request.method == "POST"):
      if(form.is_valid()):
         cleaned = form.cleaned_data
         title = cleaned['title']
         min_buy_in = cleaned['min_buy_in']
         max_buy_in = cleaned['max_buy_in']
         currency = cleaned['currency']
         game = Game (
            title=title,
            min_buy_in=min_buy_in,
            max_buy_in=max_buy_in,
            currency=currency,
            user=user,
            )

         game.save()
         form = GameForm()
         messages.success(request, "Game {0} successfully added".format(game))

   games = (Game.objects.filter(public=True) | Game.objects.filter(user=user)).filter(deleted=False)
   context = {
      'games': games,
      'form': form,
   }
   return render(request, 'games/list.html', context)

@login_required
def delete(request, pk):
   print("in delete()")
   user = request.user

   game = Game.objects.get(pk=pk)

   if(game.user.id != user.id):
      messages.error(request, "Unable to delete {0}. Not the user for this game.".format(game))
      return redirect('games:list')

   game.deleted = True

   game.save()

   messages.success(request, "Game {0} successfully deleted".format(game))
   return redirect('games:list')
