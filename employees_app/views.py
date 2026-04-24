from django.shortcuts import render
from .models import Employee
from django.db.models import Avg, Q, Count
from datetime import date


def employee_overview(request):

    # Hier die entsprechenden Filter anlegen und die context-Variable definieren, um die Daten an das Template zu übergeben
    worker_list = Employee.objects.values(
        'name', 'salary', 'department__name')

    hight_salary = Employee.objects.all().filter(
        salary__gt=3000).values('name', 'salary', 'department__name')

    number_hight_salary = Employee.objects.all().filter(
        salary__gte=5000).count()

    all_emloyee_sales = Employee.objects.all().filter(
        department__name='Sales').aggregate(Avg('salary'))

    employees_before_2021 = Employee.objects.filter(
        hire_date__lte=date(2021, 1, 1)
    ).exclude(department__name='HR').values('name', 'department__name', 'hire_date')
    print(employees_before_2021)

    return render(request, 'employee_list.html', {'worker_list': worker_list, 'hight_salary': hight_salary, 'number_hight_salary': number_hight_salary, 'all_emloyee_sales': all_emloyee_sales, 'employees_before_2021': employees_before_2021})
