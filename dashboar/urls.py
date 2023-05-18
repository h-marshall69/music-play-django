from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_music, name='upload_music'),
    path('logout/', views.exit, name='exit'),
    path('register/', views.register, name='register'),
    path('music/', views.music_list, name='music_list'),
]
