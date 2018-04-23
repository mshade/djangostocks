from django.shortcuts import render, HttpResponse
from django.conf import settings
import requests
import json

# Create your views here.

# example:
# def home(request):
#     context = { 'message': 'Hello' }
#     return render(request, 'quotes/home.html', context)

def home(request):
    try:
        response = requests.get(settings.QUOTES_URL, timeout=1)
        quotes_list = response.json()

        return render(request, 'quotes/home.html', {'context': quotes_list})
    except:
        return HttpResponse("""
        Problem retreiving JSON. Is QUOTES_URL correct?
        """, status=500)

def symbol(request, stock_symbol):
    try:
        response = requests.get(settings.QUOTES_URL, timeout=1)
        quotes_list = response.json()
        company_data = {}

        for company in quotes_list:
            if stock_symbol in company['Symbol']:
                company_data = company
                # Quit looking if we hit a match
                break

        if company_data:
            return render(request, 'quotes/symbol.html', {'context': company_data})
        else:
            return render(request, 'quotes/404.html', status="404")
    except:
        return HttpResponse("""
        Problem retreiving JSON. Is QUOTES_URL correct?
        """, status=500)

