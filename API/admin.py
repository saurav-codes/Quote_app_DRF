from django.contrib import admin
from API.models import Quote

# Register your models here.

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display= ['id','quote_text','author']
