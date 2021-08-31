from django.contrib import admin
from django.urls import include, path

# Views
from AMCE import views

app_name = "AMCE"
urlpatterns = [

path('MG1/', views.MG1, name = "MG1"),
path('', views.index, name = 'index'),
path('registro/', views.registro, name = 'registro'),
path('feed/', views.feed, name = 'feed'),
path('paso1-1/', views.post1_1, name = 'post1_1'),
path('paso1-2/', views.post1_2, name = 'post1_2'),
path('paso1-3/', views.post1_3, name = 'post1_3'),
path('paso1-4/', views.post1_4, name = 'post1_4'),
path('profile/', views.profile, name = 'profile'),
path('profile/<str:username>', views.profile, name = 'profile'),

]

