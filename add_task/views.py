from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from .models import *


class AddTaskForm1View(View):

    def get(self, request):
        form_employee = AddTaskEmployeeForm()
        form_client_data = AddTaskClientDataForm()
        return render(request, 'add_task/add_task_page1.html', {'form_employee': form_employee,
                                                               'form_client_data': form_client_data})

    def post(self, request):
        form_employee = AddTaskEmployeeForm(request.POST)
        form_client_data = AddTaskClientDataForm(request.POST)
        if form_employee.is_valid() and form_client_data.is_valid():
            employee_receiving = form_employee.cleaned_data['employee_receiving']
            employee_service = form_employee.cleaned_data['employee_service']
            client_name = form_client_data.cleaned_data['client_name']
            client_surname = form_client_data.cleaned_data['client_surname']
            client_phone = form_client_data.cleaned_data['client_phone']
            client_mail = form_client_data.cleaned_data['client_mail']
            Clients.objects.create(name=client_name, surname=client_surname,
                                   phone_number=client_phone, email_address=client_mail)
            Tasks.objects.create(employee_receiving=Employees.objects.get(id=employee_receiving),
                                 employee_service=Employees.objects.get(id=employee_service),
                                 client=Clients.objects.get(name=client_name,
                                                            surname=client_surname, phone_number=client_phone))
            return redirect('add_task_2')
        return render(request, 'add_task/add_task_page1.html', {'form_employee': form_employee,
                                                                'form_client_data': form_client_data})


class AddTaskForm2View(View):

    def get(self, request):
        form_bicycle_details = AddTaskBicycleDetailsForm()
        form_defects = AddTaskDefectsForm()
        form_parts = AddTaskPartsForm()
        return render(request, 'add_task/add_task_page2.html', {'form_bicycle_details': form_bicycle_details,
                                                                'form_defects': form_defects,
                                                                'form_parts': form_parts})

    def post(self, request):
        form_bicycle_details = AddTaskBicycleDetailsForm(request.POST)
        form_defects = AddTaskDefectsForm(request.POST)
        form_parts = AddTaskPartsForm(request.POST)
        if form_bicycle_details.is_valid() and form_defects.is_valid() and form_parts.is_valid():
            bicycle_name = form_bicycle_details.cleaned_data['bicycle_name']
            bicycle_year = form_bicycle_details.cleaned_data['bicycle_year']
            defects = form_defects.cleaned_data['defect']
            parts = form_parts.cleaned_data['part']
            t = Tasks.objects.last()
            t.bicycle_name = bicycle_name
            t.bicycle_year = bicycle_year
            t.save()
            for defect in defects:
                TasksDefects.objects.create(task=t, defect=defect)
            for part in parts:
                TasksParts.objects.create(task=t, part=part)
            return render(request, 'add_task/add_task_page3.html')
        return render(request, 'add_task/add_task_page2.html', {'form_bicycle_details': form_bicycle_details,
                                                                'form_defects': form_defects,
                                                                'form_parts': form_parts})
