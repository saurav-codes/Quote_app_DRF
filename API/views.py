from API.serializer import QuoteSerializer
from rest_framework import generics
from API.models import Quote

# Create your views here.

class QuoteList(generics.ListCreateAPIView):
    queryset= Quote.objects.all()
    serializer_class= QuoteSerializer

class Quote_retrieve_update_destroy(generics.RetrieveUpdateDestroyAPIView):
    queryset= Quote.objects.all()
    serializer_class= QuoteSerializer