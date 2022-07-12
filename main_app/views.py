from django.shortcuts import HttpResponse, render


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def teams(request):
    return render(request, 'teams/index.html')