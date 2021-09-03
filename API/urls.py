from django.urls import path
from API import views

urlpatterns = [
    path('quotes',views.QuoteList.as_view()),
    path('quote/<int:id>/',views.QuoteList.as_view()),
]
