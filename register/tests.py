from django.test import TestCase
from django.test import Client
from .models import employee, employer
# Create your tests here.

class EmployerRegistrationTest(TestCase):
    def setup(self):
        employer.objects.create(name='Yektanet', opening=1396, pswd='1234', addr='Tehran', phone='12345678' )

    def test_new_employer_registeration(self):
        c = Client()
        response = c.post('/register/employer', {'name':'Dotanet', 'opening': 1400, 'pswd': '4321', 'addr': 'shomal', 'phone':'98765432'} )

        self.assertEqual(response.status_code, 200)

    def test_employer_multi_registration(self):
        c = Client()
        employer.objects.create(name='Yektanet', opening=1396, pswd='1234', addr='Tehran', phone='12345678')
        response = c.post('/register/employer',
                          {'name': 'Yektanet', 'opening': 1400, 'pswd': '4321', 'addr': 'shomal', 'phone': '98765432'})

        self.assertEqual(response.status_code, 208)