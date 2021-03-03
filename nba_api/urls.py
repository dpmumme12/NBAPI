from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('TeamSearch/<str:team>/showStats=<str:showStats>',views.teamSearch, name ='teamSearch')
]