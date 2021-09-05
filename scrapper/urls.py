from django.urls import path
from scrapper import views

urlpatterns = [
    path('',views.index),
    path('scrape', views.quote_scraper),
]
