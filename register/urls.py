from django.urls import path

from . import views

urlpatterns = [
    path('employer', views.register_an_employer, name= 'reg_an_employer'),
    path('employee', views.register_an_employee, name='reg_an_employee')
]