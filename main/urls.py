from django.urls import path

from main import views

app_name = 'api'

urlpatterns = [
    path('', views.companies_view, name='companies-view'),
    path('add-employee/<str:company_id>', views.add_employee, name='add-employee'),
]
