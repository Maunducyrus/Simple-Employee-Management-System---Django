from django.urls import path
from .views import create_employee, update_employee, delete_employee, list_employees
urlpatterns = [
    path('', list_employees, name='list'),
    path('create/', create_employee, name='create'),
    path('update/<int:pk>/', update_employee, name='update'),
    path('delete/<int:pk>/', delete_employee, name='delete'),
]

# This code defines the URL patterns for the CRUD application. 
# It maps URLs to their corresponding views, allowing users to create, update, delete, and list employees.
