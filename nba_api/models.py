from django.db import models

# Create your models here.
class players(models.Model):
    name = models.CharField(max_length=255)
    team = models.CharField(max_length=50)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=5)
    position = models.CharField(max_length=2)
    college = models.CharField(max_length=100)
    

class statistics(models.Model):
    Year = models.CharField(max_length=20)
    team = models.CharField(max_length=50)
    avg_points = models.CharField(max_length=10)
    avg_assist = models.CharField(max_length=10)
    avg_rebounds = models.CharField(max_length=10)
    avg_steals = models.CharField(max_length=10)
    avg_blocks = models.CharField(max_length=10)
    avg_turnovers = models.CharField(max_length=10)
    FG_percentage = models.CharField(max_length=10)
    TP_percantage = models.CharField(max_length=10)
    player = models.ForeignKey('players', on_delete=models.CASCADE)
