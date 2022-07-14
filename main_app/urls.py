from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('players/', views.player_index, name='index'),
    path('players/<int:player_id>/', views.player_detail, name='player_detail'),
    path('players/register/', views.PlayerRegister.as_view(), name='player_register'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='player_update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='player_delete'),
    path('accounts/signup/', views.signup, name='signup')
]