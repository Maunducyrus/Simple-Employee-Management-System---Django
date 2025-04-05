from django.urls import path
from .views import create_employee, update_employee, delete_employee, list_employees

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('create/', create_employee, name='create'),
    path('update/<int:pk>/', update_employee, name='update'),
    path('delete/<int:pk>/', delete_employee, name='delete'),
]

urlpatterns = [
   path('', Home, name='home'), 
]
