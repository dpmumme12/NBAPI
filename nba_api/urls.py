from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('TeamSearch/<str:team>/showStats=<str:showStats>/apiKey=<str:apiKey>',views.teamSearch, name ='teamSearch'),
    path('PlayerSearch/<str:player>/apiKey=<str:apiKey>',views.playerSearch, name ='playerSearch'),
    path('statsSearch/<str:id>/apiKey=<str:apiKey>',views.statsSearch, name ='statsSearch'),
    path('Register',views.register, name ='register'),
    path('Login',views.login_view, name ='login')
]
