from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
from .models import players, statistics, user
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.urls import reverse
from .functions import r

# Create your views here.
def index(request):
   return JsonResponse({
            "results":[
            {"error": "At least one recipient required.",},{
            "tyson": {"points": 23, "rebounds": 12}}]}, status=401)

def register(request):
   if request.method == "POST":
      username = request.POST["username"]
      email = request.POST["email"]

      # Ensure password matches confirmation
      password = request.POST["password"]
      confirmation = request.POST["confirmation"]
      if password != confirmation:
         return render(request, "auctions/register.html", {
               "message": "Passwords must match."
         })

      # Attempt to create new user
      try:
         user = user.objects.create_user(username, email, password)
         user.save()
      except IntegrityError:
         return render(request, "auctions/register.html", {
               "message": "Username already taken."
         })
      login(request, user)
      return HttpResponseRedirect(reverse("index"))
   else:
      return render(request, "nba_api/register.html")


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


def playerSearch(request,player):

   objects = players.objects.filter(name__istartswith=player)

   return JsonResponse({'results':
            [obj.serialize_players() for obj in objects]
   })


def statsSearch(request,id):
   
   objects = players.objects.filter(id=id)

   return JsonResponse({'results':
            [obj.serialize_stats() for obj in objects]
   })