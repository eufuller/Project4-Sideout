from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# TEAMS = (
#     ('A', 'Aces'),
#     ('B', 'Busta Spike'),
#     ('C', 'Chewblocka'),
#     ('D', 'Dig This')
# )
# Create your models here.


# class Team(models.Model):
#     name = models.CharField(
#         max_length=1,
#         choices=TEAMS,
#         default=""
#     )
#     games = models.DateField()
#     registered = models.BooleanField()

#     def __str__(self):
#         return self.name

class Player(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    team_name = models.CharField(max_length=100)
    games_played = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'player_id': self.id})