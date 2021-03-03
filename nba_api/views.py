from django.shortcuts import render
from django.http import JsonResponse
from .models import players, statistics
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from urllib import parse

# Create your views here.
def index(request):
   return JsonResponse({
            "results":[
            {"error": "At least one recipient required.",},{
            "tyson": {"points": 23, "rebounds": 12}}]}, status=401)

def teamSearch(request,team,showStats):

   objects = players.objects.filter(team=team)

   if showStats == 'true':
      return JsonResponse({'results':
            [obj.serialize_all() for obj in objects]
   })

   else:  
      return JsonResponse({'results':
            [obj.serialize_players() for obj in objects]
   })

def playerSearch(request):
   pass

def statsSearch(request):
   pass