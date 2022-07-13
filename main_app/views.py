from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def player_index(request):
    players = Player.objects.all()
    #players = player.objects.filter(user=request.user) #only shows each user their own player.
    return render(request, 'players/index.html', { 'players': players })

def player_detail(request, player_id):
    player = Player.objects.get(id=player_id) 
    return render(request, 'players/detail.html', { 'player': player })

class PlayerRegister(CreateView):
    model = Player
    fields = '__all__'

class PlayerUpdate(UpdateView):
    model = Player
    fields = '__all__'

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players/'

