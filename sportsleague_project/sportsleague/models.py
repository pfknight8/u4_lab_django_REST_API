from django.db import models

# Create your models here.
class Conference(models.Model):
  name = models.CharField(max_length=100)
  league = models.CharField(max_length=100)
  founded = models.DateField()

  def __str__(self):
    return self.name

class Division(models.Model):
  name = models.CharField(max_length=100)
  conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='conferences')

  def __str__(self):
    return self.name

class Team(models.Model):
  name = models.CharField(max_length=50)
  logo_url = models.CharField(max_length=200)
  location = models.CharField(max_length=100)
  division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='divisions')
  wins = models.IntegerField()
  loses = models.IntegerField()
  ot_loss = models.IntegerField() #ties count as ot loss.

  def __str__(self):
    return self.name

class Player(models.Model):
  name = models.CharField(max_length=100)
  team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='teams')
  birthdate = models.DateField()

  def __str__(self):
    return self.name
