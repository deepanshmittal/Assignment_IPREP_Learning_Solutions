from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.


def companies_view(request):
    return render(request, 'companies.html', {"companies": Company.objects.all(),
                                              "employees": Employee.objects.all().order_by('first_name', 'last_name')})


def add_employee(request, company_id=None):
    if request.method == "POST":
        id = int(request.POST.get('employee'))
        employee = Employee.objects.get(id=id)
        employee.company = Company.objects.get(id=int(company_id))
        employee.save()
        return redirect('/')
    return render(request, 'add_employee.html',
                  {"employees": Employee.objects.filter(company__isnull=True).order_by('first_name', 'last_name')})
