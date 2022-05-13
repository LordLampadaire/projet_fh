from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index_hero/',views.index_hero),
    path('ajout/', views.ajout),
    path('fh/details/<int:id>/', views.details),
    path('fh/delete/<int:id>/', views.delete),
    path('fh/update/<int:id>/', views.update),
    path('updatetraitement/<int:id>/', views.updatetraitement),
    path('ajout_hero/', views.ajout_hero),
    path('fh/details_hero/<int:id>/', views.details_hero),
    path('fh/delete_hero/<int:id>/', views.delete_hero),
    path('fh/update_hero/<int:id>/', views.update_hero),
    path('updatetraitement_hero/<int:id>/', views.updatetraitement_hero),
]
