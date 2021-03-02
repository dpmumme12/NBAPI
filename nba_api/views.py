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

def load(request):

   objects = players.objects.all()

   
   return JsonResponse({'results':
            [obj.serialize() for obj in objects]
   })