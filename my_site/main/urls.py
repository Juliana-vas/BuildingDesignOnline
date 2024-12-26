from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('index.html', views.index),
    path('house.html', views.house),
    path('building.html', views.building),
    path('about.html', views.about),
]
