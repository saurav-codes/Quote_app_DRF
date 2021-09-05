from django.core.management.base import BaseCommand
from API.models import Quote
from scrapper.web_scrapper import scrap_quotes

class Command(BaseCommand):
    help= '.........'

    def add_arguments(self, parser):
        parser.add_argument('category')
        parser.add_argument('quantity')

    def handle(self,*args, **kwargs):
        category= kwargs.get('category')
        quantity= kwargs.get('quantity')
        rec_d = scrap_quotes(category,int(quantity)) 
        for key,value in rec_d.items():
            quote_obj= Quote(quote_text= key, author= value)
            quote_obj.save()
        print('Done...!')