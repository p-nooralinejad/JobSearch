from django.urls import path

from . import views

urlpatterns = [
    path('advertise', views.post_advertise, name= 'post_an_ad'),
    path('apply', views.apply_for_advertise, name='apply_for_an_ad'),
    path('get_all_ads', views.get_all_advertise, name='get_all_ads'),
    path('get_applicant', views.get_applicant_for_advertise, name='get_all_app'),
    path('edit_prof_employer', views.edit_profile_employer, name='edit_employer'),
    path('edit_prof_employee', views.edit_profile_employee, name='edit_employee'),
    path('edit_ad', views.edit_advertise, name='edit_ad')
]