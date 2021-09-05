from django.http.response import HttpResponse  

# Create your views here.

def index(request):
    return HttpResponse("Type ' < python manage.py category quantity > ' to scrap data")

