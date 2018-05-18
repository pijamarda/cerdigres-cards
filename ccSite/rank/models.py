from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Card(models.Model):
    card_text = models.CharField(max_length=200)
    def __str__(self):
        return self.card_text

class Rulebook(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='name')
    description_text = models.CharField(max_length=200, default='description')
    general_votes = models.IntegerField(default=0)
    valor_hot = models.IntegerField(default=0)
    valor_new = models.IntegerField(default=0)
    create_date = models.DateTimeField('date created',default=timezone.now)
    modified_date = models.DateTimeField('date modified',default=timezone.now)
    recomended_age_min = models.IntegerField(default=0)
    recomended_age_max = models.IntegerField(default=99)
    num_players_min = models.IntegerField(default=1)
    num_players_max = models.IntegerField(default=5)
    skill_rate = models.IntegerField(default=0)
    luck_rate = models.IntegerField(default=0)
    game_time_median = models.IntegerField(default=30)
    def __str__(self):
        return self.name