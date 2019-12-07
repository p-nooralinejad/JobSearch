from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.datetime_safe import datetime

from advertise.models import advertise, application
from register.models import employer, employee


def post_advertise(request):
    req_data = request.POST
    owner = employer.objects.get(name = req_data['employer_name'])
    title = req_data['title']
    Description = req_data['desc']
    expiree_date = datetime.datetime.strptime(req_data['exp_date'], "%Y-%m-%d").date()
    field = req_data['field']
    salary = req_data['salary']
    hours = req_data['hours']

    advertise.objects.create(owner=owner, title=title, Description=Description\
                             , expiree_date=expiree_date, field=field, salary=salary, hours=hours)
    advertise.save()

    return JsonResponse({'result':'OK'}, status=200)


def apply_for_advertise(request):
    req_data = request.POST
    applicant = employee.objects.get(username=req_data['user'])
    adv_id = advertise.objects.get(adv_id=req_data['adv_id'])

    application.objects.create(applicant=applicant, adv_id=adv_id)
    application.save()

    return JsonResponse({'result':'OK'}, status=200)


def get_all_advertise(request):
    req_data = request.GET
    resp = []
    if req_data['search'] == 'by_title':
        ads = advertise.objects.get(title=req_data['title'])
        for adv in ads:
            resp.append(str(adv))

    elif req_data['search'] == 'by_salary':
        ads = advertise.objects.all()
        for adv in ads:
            if req_data['min_salary'] <= adv.salary and adv.salary <= req_data['max_salary']:
                resp.append(str(adv))
    else:
        resp = advertise.objects.all()

    return JsonResponse({'result':'OK', 'ads':str(resp)}, status=200)


def get_applicant_for_advertise(request):
    req_data = request.GET
    adv = advertise.objects.get(adv_id=req_data)
    if req_data.name != adv.owner.name:
        return JsonResponse({'result':'Unauthorized access'}, status=403)
    applications = application.objects.get(adv_id=req_data['adv_id'])
    users = []
    for app in applications:
        users.append(str(app))

    return JsonResponse({'result':'OK', 'applicants':str(users)},status=200)


def edit_profile_employer(request):
    req_data = request.POST
    emp = employer.objects.get(name=req_data['name'])

    if req_data['new_pswd'] != None:
        emp.pswd = req_data['new_pswd']

    if req_data['new_phone'] != None:
        emp.phone = req_data['new_phone']

    if req_data['new_addr'] != None:
        emp.addr = req_data['new_addr']

    if req_data['new_field'] != None:
        emp.field = req_data['new_field']

    emp.save()
    return JsonResponse({'result':'OK'}, status=200)


def edit_profile_employee(request):
    req_data = request.POST
    emp = employee.objects.get(username=req_data['user'])

    if req_data['new_pswd'] != None:
        emp.pswd = req_data['new_pswd']

    if req_data['new_field'] != None:
        emp.field = req_data['new_field']

    emp.save()
    return JsonResponse({'result': 'OK'}, status=200)


def edit_advertise(request):
    req_data = request.POST
    adv = advertise.objects.get(adv_id=req_data['adv_id'])
    if adv.owner.name != req_data['name']:
        return JsonResponse({'result':'This is not your advertisement, you can not edit it.'}, status=403)
    '''
    title = models.CharField(max_length=300)
    field = models.CharField(max_length=400)
    salary = models.IntegerField()
    hours = models.IntegerField()
    Description = models.CharField(max_length=1000)
    '''
    if req_data['new_desc'] != None:
        adv.Description = req_data['new_desc']

    if req_data['new_salary'] != None:
        adv.salary = req_data['new_salary']

    if req_data['new_title'] != None:
        adv.title = req_data['new_title']

    if req_data['new_hours'] != None:
        adv.hours = req_data['new_hours']

    if req_data['new_field'] != None:
        adv.field = req_data['new_field']

    adv.save()

    return JsonResponse({'result':'OK'}, status=200)
