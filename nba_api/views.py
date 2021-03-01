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

   print(list(statistics.objects.all().values()))

   return JsonResponse({'results':
            'h'
            #[obj.serialize() for obj in objects]
   })