from django.urls import include, path, re_path
from rest_framework import routers
from . import views

urlpatterns = [
    path('getallstock/',views.getAllStock),
    path('getdrinkstock/<str:drinkname>/',views.getDrinkStock),
    path('adddrinkstock/<str:drinkname>/',views.addDrinkStock)
]