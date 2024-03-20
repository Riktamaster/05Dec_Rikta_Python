from django.shortcuts import render
from .models import *
from .forms import *

def main_page(request):
    return render(request, 'main_page.html')

def search_results(request):
    query = request.GET.get('q')
    if query:
        # Perform case-insensitive search for product name
        results = product_sub_cat.objects.filter(product__product_name__icontains=query)
    else:
        results = []
    return render(request, 'search_results.html', {'results': results, 'query': query})
