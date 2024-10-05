import random 
from django.shortcuts import render
def random_quote_view(request):
    with open('quotes.txt','r',encoding='utf-8') as file:
        quotes = file.readlines()
    random_quote = random.choice(quotes).strip()
    return render(request,'quotes/quote.html',{'quote':random_quote})
# Create your views here.
