from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import employee
from .models import employer
# Create your views here.

def register_an_employer(request):
    emp_data = request.POST

    if employer.objects.filter(name=emp_data['name']).exists():
        return JsonResponse({'result':'employer already exists'},status=208)

    employer_instance = employer.objects.create(name=emp_data['name']\
                                                ,opening=emp_data['opening']\
                                                ,pswd=emp_data['pswd']\
                                                ,addr=emp_data['addr']\
                                                ,phone=emp_data['phone'])
    employer_instance.save()
    return JsonResponse({'result':'OK'}, status=200)

def register_an_employee(request):
    emp_data = request.POST

    if employee.objects.filter(username=emp_data['username']).exists():
        return JsonResponse({'result':'user already exists'}, status=208)

    employee_instance = employee.objects.create(first_name=emp_data['firstname']\
                                                ,surname=emp_data['surname']\
                                                ,username=emp_data['username']\
                                                ,pswd=emp_data['pswd']\
                                                ,gender=emp_data['gender']\
                                                ,age=emp_data['age'])

    employee_instance.save()
    return JsonResponse({'result': 'OK'}, status=200)