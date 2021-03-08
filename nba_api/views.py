from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect, HttpResponse
from .models import players, statistics, User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.urls import reverse
from .functions import randompassword

# Create your views here.
def index(request):
  
   return render(request, "nba_api/index.html")

def docs(request):
  
   return render(request, "nba_api/docs.html")

def account(request):
  
   return render(request, "nba_api/account.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

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
         new_user = User.objects.create_user(username=username, password=password, apiKey=apiKey)
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


def teamSearch(request,team,showStats,apiKey):

   num_results = User.objects.filter(apiKey = apiKey).count()

   if num_results == 1:

      objects = players.objects.filter(team=team)

      user = User.objects.get(apiKey = apiKey)
      user.num_of_request += 1
      user.save()

      if showStats == 'true':
         return JsonResponse({'results':
               [obj.serialize_all() for obj in objects]
      })

      else:  
         return JsonResponse({'results':
               [obj.serialize_players() for obj in objects]
      })

   else:
      return HttpResponse("Error: Invalid key given.")


def playerSearch(request,player,apiKey):

   num_results = User.objects.filter(apiKey = apiKey).count()

   if num_results == 1:

      objects = players.objects.filter(name__istartswith=player)

      user = User.objects.get(apiKey = apiKey)
      user.num_of_request += 1
      user.save()

      return JsonResponse({'results':
               [obj.serialize_players() for obj in objects]
      })
   
   else:
      return HttpResponse("Error: Invalid key given.")


def statsSearch(request,id,apiKey):

   num_results = User.objects.filter(apiKey = apiKey).count()

   if num_results == 1:
   
      objects = players.objects.filter(id=id)

      user = User.objects.get(apiKey = apiKey)
      user.num_of_request += 1
      user.save()

      return JsonResponse({'results':
               [obj.serialize_stats() for obj in objects]
      })

   else:
      return HttpResponse("Error: Invalid key given.")