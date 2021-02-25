from django.shortcuts import render
from django.http import JsonResponse
from .models import players, statistics

# Create your views here.
def index(request):
   return JsonResponse({
            "results":[
            {"error": "At least one recipient required.",},{
            "tyson": {"points": 23, "rebounds": 12}}]}, status=401)

def load(request):
   player = players()
   player.name = "kyle"
   player.position="C"
   player.team="Pelicans"
   player.weight="165"
   player.height="6-11"
   player.college="MAryland"
   
   player.save()

   stats = statistics()
   stats.team = 'Lakers'
   stats.avg_assist = '2.1'
   stats.avg_blocks = '0.4'
   stats.avg_points = '19'
   stats.avg_rebounds = '5'
   stats.avg_steals = '.2'
   stats.avg_turnovers = '4'
   stats.Year = '2015-16'
   stats.TP_percantage = '37'
   stats.FG_percentage = '45'
   stats.player = player

   stats.save()

   stats = statistics()
   stats.team = 'suns'
   stats.avg_assist = '2.1'
   stats.avg_blocks = '0.4'
   stats.avg_points = '19'
   stats.avg_rebounds = '5'
   stats.avg_steals = '.2'
   stats.avg_turnovers = '4'
   stats.Year = '2016-17'
   stats.TP_percantage = '37'
   stats.FG_percentage = '45'
   stats.player = player

   stats.save()


   return JsonResponse({
            "hello":[
            {"error": "At least one recipient required.",},{
            "tyson": {"points": 23, "rebounds": 12}}]}, status=401)