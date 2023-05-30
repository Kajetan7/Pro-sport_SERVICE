import datetime
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
            request.session['employee_receiving'] = form_employee.cleaned_data['employee_receiving']
            request.session['employee_service'] = form_employee.cleaned_data['employee_service']
            request.session['client_name'] = form_client_data.cleaned_data['client_name']
            request.session['client_surname'] = form_client_data.cleaned_data['client_surname']
            request.session['client_phone'] = form_client_data.cleaned_data['client_phone']
            request.session['client_mail'] = form_client_data.cleaned_data['client_mail']
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
            request.session['bicycle_name'] = form_bicycle_details.cleaned_data['bicycle_name']
            request.session['bicycle_year'] = form_bicycle_details.cleaned_data['bicycle_year']
            request.session['defects'] = form_defects.cleaned_data['defect']
            request.session['parts'] = form_parts.cleaned_data['part']
            return redirect('add_task_3')
        return render(request, 'add_task/add_task_page2.html', {'form_bicycle_details': form_bicycle_details,
                                                                'form_defects': form_defects,
                                                                'form_parts': form_parts})


class AddTaskForm3View(View):

    def get(self, request):
        form_additional_info = AddTaskAdditionalInfoForm()
        return render(request, 'add_task/add_task_page3.html', {'form_additional_info': form_additional_info})

    def post(self, request):
        form_additional_info = AddTaskAdditionalInfoForm(request.POST)
        print(request.POST)
        if form_additional_info.is_valid():
            request.session['priority'] = form_additional_info.cleaned_data['priority']
            request.session['reclamation'] = form_additional_info.cleaned_data['reclamation']
            request.session['payment_in_advance'] = form_additional_info.cleaned_data['payment_in_advance']
            request.session['notes'] = form_additional_info.cleaned_data['notes']
            return redirect('task_estimated_price')
        return render(request, 'add_task/add_task_page3.html', {'form_additional_info': form_additional_info})


class AddTaskEstimatedPriceView(View):

    def get(self, request):
        form_estimated_price = AddTaskEstimatedPriceForm()
        return render(request, 'add_task/add_task_page4.html', {'form_estimated_price': form_estimated_price})

    def post(self, request):
        form_estimated_price = AddTaskEstimatedPriceForm(request.POST, request.FILES)
        if form_estimated_price.is_valid():
            estimated_price = form_estimated_price.cleaned_data['estimated_price']
            estimated_time = form_estimated_price.cleaned_data['estimated_time']
            photo = form_estimated_price.cleaned_data['photo']
            Clients.objects.create(name=request.session['client_name'],
                                   surname=request.session['client_surname'],
                                   email_address=request.session['client_mail'],
                                   phone_number=request.session['client_phone'])
            Tasks.objects.create(employee_receiving=Employees.objects.get(id=request.session['employee_receiving']),
                                 employee_service=Employees.objects.get(id=request.session['employee_service']),
                                 client=Clients.objects.get(name=request.session['client_name'],
                                                            surname=request.session['client_surname'],
                                                            phone_number=request.session['client_phone']),
                                 bicycle_name=request.session['bicycle_name'],
                                 bicycle_year=request.session['bicycle_year'],
                                 priority=request.session['priority'],
                                 reclamation=request.session['reclamation'],
                                 payment_in_advance=request.session['payment_in_advance'],
                                 estimated_time=estimated_time * 60,
                                 photo=photo,
                                 notes=request.session['notes'],
                                 expected_price=estimated_price)
            for defect in request.session['defects']:
                TasksDefects.objects.create(task=Tasks.objects.last(), defect=Defects.objects.get(id=defect))
            for part in request.session['parts']:
                TasksParts.objects.create(task=Tasks.objects.last(), part=Parts.objects.get(id=part))
            return redirect('menu')
        return render(request, 'add_task/add_task_page4.html', {'form_estimated_price': form_estimated_price})


class EditTaskForm1View(View):

    def get(self, request, id):
        task = Tasks.objects.get(id=id)
        employees = Employees.objects.all()
        return render(request, 'add_task/edit_task_page1.html', {'task': task, 'employees': employees})

    def post(self, request, id):
        employee_receiving = request.POST.get('employee_receiving')
        employee_service = request.POST.get('employee_service')
        client_name = request.POST.get('client_name')
        client_surname = request.POST.get('client_surname')
        client_phone = request.POST.get('client_phone')
        client_mail = request.POST.get('client_mail')
        client = Clients.objects.get(id=Tasks.objects.get(id=id).client_id)
        client.name = client_name
        client.surname = client_surname
        client.phone_number = client_phone
        client.email_address = client_mail
        client.save()
        task = Tasks.objects.get(id=id)
        task.employee_receiving = Employees.objects.get(id=employee_receiving)
        task.employee_service = Employees.objects.get(id=employee_service)
        task.client = Clients.objects.get(name=client_name, surname=client_surname, phone_number=client_phone)
        task.save()
        return redirect('edit_task_2', id=id)


class EditTaskForm2View(View):

    def get(self, request, id):
        task = Tasks.objects.get(id=id)
        defects = Defects.objects.all()
        parts = Parts.objects.all()
        return render(request, 'add_task/edit_task_page2.html', {'task': task, 'defects': defects, 'parts': parts})

    def post(self, request, id):
        bicycle_name = request.POST.get('bicycle_name')
        bicycle_year = request.POST.get('bicycle_year')
        defects = request.POST.getlist('defects')
        parts = request.POST.getlist('parts')
        t = Tasks.objects.get(id=id)
        t.bicycle_name = bicycle_name
        t.bicycle_year = bicycle_year
        t.save()
        TasksDefects.objects.filter(task_id=id).delete()
        TasksParts.objects.filter(task_id=id).delete()
        for defect in defects:
            TasksDefects.objects.create(task=Tasks.objects.get(id=id), defect=Defects.objects.get(id=defect))
        for part in parts:
            TasksParts.objects.create(task=Tasks.objects.get(id=id), part=Parts.objects.get(id=part))
        return redirect('edit_task_3', id=id)


class EditTaskForm3View(View):

    def get(self, request, id):
        task = Tasks.objects.get(id=id)
        return render(request, 'add_task/edit_task_page3.html', {'task': task})

    def post(self, request, id):
        priority = request.POST.get('priority')
        if priority == 'on':
            priority = True
        else:
            priority = False
        reclamation = request.POST.get('reclamation')
        if reclamation == 'on':
            reclamation = True
        else:
            reclamation = False
        payment_in_advance = request.POST.get('payment_in_advance')
        notes = request.POST.get('notes')
        t = Tasks.objects.get(id=id)
        t.priority = priority
        t.reclamation = reclamation
        t.payment_in_advance = payment_in_advance
        t.notes = notes
        t.save()
        return redirect('edit_task_4', id=id)


class EditTaskForm4View(View):

    def get(self, request, id):
        task = Tasks.objects.get(id=id)
        return render(request, 'add_task/edit_task_page4.html', {'task': task})

    def post(self, request, id):
        estimated_price = request.POST.get('estimated_price')
        estimated_time_str = request.POST.get('estimated_time')
        estimated_time_calc = datetime.datetime.strptime(estimated_time_str, '%H:%M')
        total_sec = estimated_time_calc.hour*3600 + estimated_time_calc.minute*60
        estimated_time = datetime.timedelta(seconds=total_sec)
        photo = request.POST.get('photo')
        t = Tasks.objects.get(id=id)
        t.estimated_time = estimated_time
        t.expected_price = estimated_price
        if photo:
            t.photo = photo
        t.save()
        return redirect('menu')
