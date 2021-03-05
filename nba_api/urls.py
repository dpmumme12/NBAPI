from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('TeamSearch/<str:team>/showStats=<str:showStats>',views.teamSearch, name ='teamSearch'),
    path('PlayerSearch/<str:player>',views.playerSearch, name ='playerSearch'),
    path('statsSearch/<str:id>',views.statsSearch, name ='statsSearch'),
    path('Register',views.register, name ='resgister')
]
