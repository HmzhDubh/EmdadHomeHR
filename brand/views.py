from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def all_brands(request: HttpRequest):

    return render(request, 'all_brands.html')


def brand_details(request: HttpRequest):

    return render(request, 'brand_details.html')
