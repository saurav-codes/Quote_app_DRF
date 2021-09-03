from django.db import models

# Create your models here.

class Quote(models.Model):
    quote_text= models.CharField(max_length=500)
    author= models.CharField(max_length=50) 

    def __str__(self):
        return self.quote_text