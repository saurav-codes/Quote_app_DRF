from django.urls import path
from scrapper import views

urlpatterns = [
    path('',views.index), 
]
