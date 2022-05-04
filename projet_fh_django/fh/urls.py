from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('ajout/',views.ajout),
    path('details/<int:id>/', views.read),
    path('show/', views.show),
]