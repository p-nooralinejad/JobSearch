from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.datetime_safe import datetime

from advertise.models import advertise, application
from register.models import employer, employee


def post_advertise(request):
    req_data = request.POST
    if employer.objects.filter(name=req_data['employer_name']).exists() == False:
        return JsonResponse({'result':'employer not found'}, status=404)

    owner = employer.objects.get(name=req_data['employer_name'])
    title = req_data['title']
    Description = req_data['desc']
    expiree_date = datetime.strptime(req_data['exp_date'], "%Y-%m-%d").date()
    field = req_data['field']
    salary = req_data['salary']
    hours = req_data['hours']

    advertise.objects.create(owner=owner, title=title, Description=Description\
                             , expiree_date=expiree_date, field=field, salary=salary, hours=hours)


    return JsonResponse({'result':'OK'}, status=200)


def apply_for_advertise(request):
    req_data = request.POST
    if employee.objects.filter(username=req_data['user']).exists() == False:
        return JsonResponse({'result':'user not found'}, status=404)

    if advertise.objects.filter(adv_id=req_data['adv_id']).exists() == False:
        return JsonResponse({'result':'ad not found'}, status=404)

    applicant = employee.objects.get(username=req_data['user'])
    adv_id = advertise.objects.get(adv_id=req_data['adv_id'])

    application.objects.create(applicant=applicant, adv_id=adv_id)

    return JsonResponse({'result':'OK'}, status=200)


def get_all_advertise(request):
    req_data = request.GET
    resp = []
    if req_data['search'] == 'by_title':
        ads = advertise.objects.all()

        for adv in ads:
            if adv.title == req_data['title']:
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
    adv = advertise.objects.get(adv_id=req_data['adv_id'])
    if req_data['owner_name'] != adv.owner.name:
        return JsonResponse({'result':'Unauthorized access'}, status=403)

    applications = application.objects.all()
    users = []
    for app in applications:
        if app.adv_id == req_data['adv_id']:
            users.append(str(app))

    return JsonResponse({'result':'OK', 'applicants':str(users)},status=200)


def edit_profile_employer(request):
    req_data = request.POST

    emp = employer.objects.get(name=req_data['name'])

    if req_data['new_pswd'] != None:
        emp.pswd = req_data['new_pswd']

    if req_data['new_phone'] != '':
        emp.phone = req_data['new_phone']

    if req_data['new_addr'] != '':
        emp.addr = req_data['new_addr']

    if req_data['new_field'] != '':
        emp.field = req_data['new_field']

    emp.save()
    return JsonResponse({'result':'OK'}, status=200)


def edit_profile_employee(request):
    req_data = request.POST
    emp = employee.objects.get(username=req_data['user'])

    if req_data['new_pswd'] != '':
        emp.pswd = req_data['new_pswd']

    if req_data['new_field'] != '':
        emp.field = req_data['new_field']

    emp.save()
    return JsonResponse({'result': 'OK'}, status=200)


def edit_advertise(request):
    req_data = request.POST
    adv = advertise.objects.get(adv_id=req_data['adv_id'])
    if adv.owner.name != req_data['name']:
        return JsonResponse({'result':'This is not your advertisement, you can not edit it.'}, status=403)

    if req_data['new_desc'] != '':
        adv.Description = req_data['new_desc']

    if req_data['new_salary'] != -1:
        adv.salary = req_data['new_salary']

    if req_data['new_title'] != '':
        adv.title = req_data['new_title']

    if req_data['new_hours'] != -1:
        adv.hours = req_data['new_hours']

    if req_data['new_field'] != '':
        adv.field = req_data['new_field']

    adv.save()

    return JsonResponse({'result':'OK'}, status=200)
