from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def employee_profile(request: HttpRequest, emp_id):

    return render(request, 'employee_profile.html')


def all_employees(request: HttpRequest):

    return render(request, 'all_employees.html')