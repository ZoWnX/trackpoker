from django.forms import ModelForm

from .models import Game

class GameForm(ModelForm):
   class Meta:
      model = Game
      fields = ('title','currency','min_buy_in','max_buy_in')