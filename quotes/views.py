from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.

# example:
# def home(request):
#     context = { 'message': 'Hello' }
#     return render(request, 'quotes/home.html', context)

def home(request):
    response = requests.get('http://localhost:8000/static/quotes_data.json')
    quotes_list = response.json()

    return render(request, 'quotes/home.html', {'context': quotes_list})


def symbol(request, stock_symbol):
    response = requests.get('http://localhost:8000/static/quotes_data.json')
    quotes_list = response.json()
    company_data = {}

    for company in quotes_list:
        if stock_symbol in company['Symbol']:
            company_data = company
            break

    if company_data:
        return render(request, 'quotes/symbol.html', {'context': company_data})
    else:
        return render(request, 'quotes/404.html', status="404")

