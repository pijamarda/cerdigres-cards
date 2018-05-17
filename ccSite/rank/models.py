from django.db import models

class Card(models.Model):
    card_text = models.CharField(max_length=200)
    def __str__(self):
        return self.card_text

class Rulebook(models.Model):
    rulebook_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.rulebook_text