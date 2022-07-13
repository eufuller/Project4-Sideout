from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Player


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def player_index(request):
    players = Player.objects.filter(user=request.user) #only shows each user their own player.
    return render(request, 'players/index.html', { 'players': players })

@login_required
def player_detail(request, player_id):
    player = Player.objects.get(id=player_id) 
    return render(request, 'players/detail.html', { 'player': player })


class PlayerRegister(LoginRequiredMixin, CreateView):
    model = Player
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid()

class PlayerUpdate(LoginRequiredMixin, UpdateView):
    model = Player
    fields = '__all__'

class PlayerDelete(LoginRequiredMixin, DeleteView):
    model = Player
    success_url = '/players/'

def signup(request):
    error_message = ''
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
