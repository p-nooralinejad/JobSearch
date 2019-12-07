from django.test import TestCase, Client

# Create your tests here.
from advertise.models import advertise
from register.models import employer

from django.test.client import RequestFactory

class ActionTest(TestCase):

    def test_post_ad(self):
        employer.objects.create(name='Yektanet', opening=1396, pswd='1234', addr='Tehran', phone='12345678')
        c = Client()
        response = c.post('/action/advertise',{'employer_name': 'Yektanet'\
                                               ,'title' : 'test'\
                                               , 'desc': 'test'\
                                               , 'exp_date':'2020-01-01'\
                                                , 'field':'cs'\
                                                , 'salary': 1000\
                                               , 'hours': 8 })
        self.assertEqual(response.status_code, 200)

    def test_post_ad_with_not_existing_employer(self):
        employer.objects.create(name='Yektanet', opening=1396, pswd='1234', addr='Tehran', phone='12345678')
        c = Client()
        response = c.post('/action/advertise',{'employer_name': 'Dottanet'\
                                               ,'title' : 'test'\
                                               , 'desc': 'test'\
                                               , 'exp_date':'2020-01-01'\
                                                , 'field':'cs'\
                                                , 'salary': 1000\
                                               , 'hours': 8 })
        self.assertEqual(response.status_code, 404)

    def test_apply_for_ad(self):
        employer.objects.create(name='Yektanet', opening=1396, pswd='1234', addr='Tehran', phone='12345678')
        c = Client()
        response = c.post('/action/advertise',{'employer_name': 'Yektanet'\
                                               ,'title' : 'test'\
                                               , 'desc': 'test'\
                                               , 'exp_date':'2020-01-01'\
                                                , 'field':'cs'\
                                                , 'salary': 1000\
                                               , 'hours': 8 })
        response = c.post('/register/employee', \
                          {'firstname': 'Parsa', 'surname': 'Nooralinejad', 'username': 'ParsaN', 'pswd': '1234',\
                           'gender': 'M', 'age': 23})
        response = c.post('/action/apply', {'user':'ParsaN', 'adv_id':1})

        self.assertEqual(response.status_code,200)

    def test_apply_for_not_existing_ad(self):
        employer.objects.create(name='Yektanet', opening=1396, pswd='1234', addr='Tehran', phone='12345678')
        c = Client()
        response = c.post('/action/advertise', {'employer_name': 'Yektanet' \
            , 'title': 'test' \
            , 'desc': 'test' \
            , 'exp_date': '2020-01-01' \
            , 'field': 'cs' \
            , 'salary': 1000 \
            , 'hours': 8})
        response = c.post('/register/employee', \
                          {'firstname': 'Parsa', 'surname': 'Nooralinejad', 'username': 'ParsaN', 'pswd': '1234', \
                           'gender': 'M', 'age': 23})
        response = c.post('/action/apply', {'user': 'ParsaN', 'adv_id': 2})

        self.assertEqual(response.status_code, 404)

    def test_apply_with_not_existing_user(self):
        employer.objects.create(name='Yektanet', opening=1396, pswd='1234', addr='Tehran', phone='12345678')
        c = Client()
        response = c.post('/action/advertise', {'employer_name': 'Yektanet' \
            , 'title': 'test' \
            , 'desc': 'test' \
            , 'exp_date': '2020-01-01' \
            , 'field': 'cs' \
            , 'salary': 1000 \
            , 'hours': 8})
        response = c.post('/register/employee', \
                          {'firstname': 'Parsa', 'surname': 'Nooralinejad', 'username': 'ParsaN', 'pswd': '1234', \
                           'gender': 'M', 'age': 23})
        response = c.post('/action/apply', {'user': 'ParsaM', 'adv_id': 1})

        self.assertEqual(response.status_code, 404)

    def test_get_all_ads(self):
        employer.objects.create(name='Yektanet', opening=1396, pswd='1234', addr='Tehran', phone='12345678')
        c = Client()
        response = c.get('/action/get_all_ads', {'search':'by_title', 'title' : 'test'})
        self.assertEqual(response.status_code, 200)

    def test_get_all_applicant_for_ad(self):
        employer.objects.create(name='Yektanet', opening=1396, pswd='1234', addr='Tehran', phone='12345678')
        c = Client()
        response = c.post('/action/advertise', {'employer_name': 'Yektanet' \
            , 'title': 'test' \
            , 'desc': 'test' \
            , 'exp_date': '2020-01-01' \
            , 'field': 'cs' \
            , 'salary': 1000 \
            , 'hours': 8})
        response = c.post('/register/employee', \
                          {'firstname': 'Parsa', 'surname': 'Nooralinejad', 'username': 'ParsaN', 'pswd': '1234', \
                           'gender': 'M', 'age': 23})
        response = c.post('/action/apply', {'user': 'ParsaN', 'adv_id': 1})

        response = c.get('/action/get_applicant', {'owner_name':'Yektanet', 'adv_id':1})

        self.assertEqual(response.status_code, 200)

    def test_get_all_applicant_for_ad_unauthorized(self):
        employer.objects.create(name='Yektanet', opening=1396, pswd='1234', addr='Tehran', phone='12345678')
        c = Client()
        response = c.post('/action/advertise', {'employer_name': 'Yektanet' \
            , 'title': 'test' \
            , 'desc': 'test' \
            , 'exp_date': '2020-01-01' \
            , 'field': 'cs' \
            , 'salary': 1000 \
            , 'hours': 8})
        response = c.post('/register/employee', \
                          {'firstname': 'Parsa', 'surname': 'Nooralinejad', 'username': 'ParsaN', 'pswd': '1234', \
                           'gender': 'M', 'age': 23})
        response = c.post('/action/apply', {'user': 'ParsaN', 'adv_id': 1})

        response = c.get('/action/get_applicant', {'owner_name': 'Dottanet', 'adv_id': 1})

        self.assertEqual(response.status_code, 403)

    def test_edit_profile_employer(self):
        employer.objects.create(name='Yektanet', opening=1396, pswd='1234', addr='Tehran', phone='12345678')
        c = Client()
        response = c.post('/action/advertise', {'employer_name': 'Yektanet' \
            , 'title': 'test' \
            , 'desc': 'test' \
            , 'exp_date': '2020-01-01' \
            , 'field': 'cs' \
            , 'salary': 1000 \
            , 'hours': 8})
        response = c.post('/action/edit_prof_employer', {'name': 'Yektanet', 'new_pswd': '4312',\
                                                         'new_phone':'', 'new_addr':'', 'new_field':''})

        self.assertEqual(response.status_code,200)

    def test_edit_profile_employee(self):
        employer.objects.create(name='Yektanet', opening=1396, pswd='1234', addr='Tehran', phone='12345678')
        c = Client()
        response = c.post('/register/employee',\
                          {'firstname': 'Parsa', 'surname': 'Nooralinejad', 'username': 'ParsaN', 'pswd': '1234', \
                           'gender': 'M', 'age': 23})
        response = c.post('/action/edit_prof_employee', {'user': 'ParsaN', 'new_pswd': '4312', 'new_field': ''})

        self.assertEqual(response.status_code,200)

    def test_edit_advertise(self):
        employer.objects.create(name='Yektanet', opening=1396, pswd='1234', addr='Tehran', phone='12345678')
        c = Client()
        response = c.post('/action/advertise', {'employer_name': 'Yektanet' \
            , 'title': 'test' \
            , 'desc': 'test' \
            , 'exp_date': '2020-01-01' \
            , 'field': 'cs' \
            , 'salary': 1000 \
            , 'hours': 8})
        response = c.post('/action/edit_ad', {'name': 'Yektanet', 'adv_id':1, 'new_desc': 'lkadfj', \
                                                         'new_salary': -1, 'new_title': '', 'new_field': '', 'new_hours':-1})

        self.assertEqual(response.status_code, 200)