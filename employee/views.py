from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def employee_profile(request: HttpRequest):

    return render(request, 'employee_profile.html')
