from rest_framework import serializers
from API.models import Quote

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Quote
        fields= ['id','quote_text','author']