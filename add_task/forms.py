from django import forms
from django.core.exceptions import ValidationError
from add_task.models import *


class AddTaskForm1(forms.Form):
    employees = Employees.objects.all()

    list = []
    for employee in employees:
        list.append((employee.id, f"{employee.name} {employee.surname}"))

    CHOICES = tuple(list)

    employee_receiving = forms.ChoiceField(choices=CHOICES)
    employee_service = forms.ChoiceField(choices=CHOICES)
    client = forms.CharField(max_length=128)

