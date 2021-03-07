from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
from .models import players, statistics, User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.urls import reverse
from .functions import randompassword

# Create your views here.
def index(request):
  
   return JsonResponse({
            "results":[
            {"error": "At least one recipient required.",},{
            "tyson": {"points": 23, "rebounds": 12}}]}, status=401)

def register(request):
   if request.method == "POST":
      username = request.POST["username"]

      # Ensure password matches confirmation
      password = request.POST["password"]
      confirmation = request.POST["confirmation"]
      if password != confirmation:
         return render(request, "nba_api/register.html", {
               "message": "Passwords must match."
         })

      # Attempt to create new user
      try:
         apiKey = randompassword()
         new_user = User.objects.create_user(username, password, apiKey=apiKey)
         new_user.save()
      except IntegrityError:
         return render(request, "nba_api/register.html", {
               "message": "Username already taken."
         })
      login(request, new_user)
      return HttpResponseRedirect(reverse("index"))
   else:
      
      return render(request, "nba_api/register.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "nba_api/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "nba_api/login.html")


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