from django.http.response import HttpResponse 
from scrapper.web_scrapper import scrap_quotes
from API.serializer import QuoteSerializer

# Create your views here.

def index(request):
    return HttpResponse('web scrapper')



def quote_scraper(quantity=10, category='hello'):
    # get the quotes
    quotes_dict= scrap_quotes(category,quantity)
    # saves to DB
    if quotes_dict:
        for key,value in quotes_dict.items():
            serialized_data= QuoteSerializer(data={'quote_text':key,'author':value})
            if serialized_data.is_valid():
                serialized_data.save()
                print('saved success')