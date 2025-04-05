from django.shortcuts import render
from .forms import EmployeeForm
from django.shortcuts import redirect
from .models import Employee

# Create view
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm()
    return render(request, 'create.html', {'form': form})

# List view
def list_employees(request):
    employees = Employee.objects.all()
    return render(request, 'list.html', {'employees': employees})

# Update view
def update_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('list')
        
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update.html', {'form': form})
