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
                TasksDefects.objects.create(task=t, defect=Defects.objects.get(id=defect))
            for part in parts:
                TasksParts.objects.create(task=t, part=Parts.objects.get(id=part))
            return redirect('add_task_3')
        return render(request, 'add_task/add_task_page2.html', {'form_bicycle_details': form_bicycle_details,
                                                                'form_defects': form_defects,
                                                                'form_parts': form_parts})


class AddTaskForm3View(View):

    def get(self, request):
        form_additional_info = AddTaskAdditionalInfoForm()
        return render(request, 'add_task/add_task_page3.html', {'form_additional_info': form_additional_info})

    def post(self, request):
        form_additional_info = AddTaskAdditionalInfoForm(request.POST, request.FILES)
        print(request.POST)
        if form_additional_info.is_valid():
            priority = form_additional_info.cleaned_data['priority']
            reclamation = form_additional_info.cleaned_data['reclamation']
            payment_in_advance = form_additional_info.cleaned_data['payment_in_advance']
            estimated_time = form_additional_info.cleaned_data['estimated_time']
            photo = form_additional_info.cleaned_data['photo']
            print(estimated_time)
            print(estimated_time.seconds)
            notes = form_additional_info.cleaned_data['notes']
            t = Tasks.objects.last()
            t.priority = priority
            t.reclamation = reclamation
            t.payment_in_advance = payment_in_advance
            t.estimated_time = estimated_time * 60
            t.notes = notes
            t.photo = photo
            t.save()
            return redirect('task_estimated_price')
        return render(request, 'add_task/add_task_page3.html', {'form_additional_info': form_additional_info})


class AddTaskEstimatedPriceView(View):

    def get(self, request):
        form_estimated_price = AddTaskEstimatedPriceForm()
        return render(request, 'add_task/add_task_page4.html', {'form_estimated_price': form_estimated_price})

    def post(self, request):
        form_estimated_price = AddTaskEstimatedPriceForm(request.POST)
        if form_estimated_price.is_valid():
            estimated_price = form_estimated_price.cleaned_data['estimated_price']
            t = Tasks.objects.last()
            t.expected_price = estimated_price
            t.save()
            return redirect('menu')
        return render(request, 'add_task/add_task_page4.html', {'form_estimated_price': form_estimated_price})