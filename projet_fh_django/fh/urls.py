from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ajout/', views.ajout),
    path('fh/details/<int:id>/', views.details),
    path('show/', views.show),
]
