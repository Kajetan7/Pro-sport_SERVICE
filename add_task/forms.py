from django import forms
from django.core.exceptions import ValidationError
from add_task.models import *


class AddTaskEmployeeForm(forms.Form):

    employees = Employees.objects.all()

    list = []
    for employee in employees:
        list.append((employee.id, employee))

    CHOICES = tuple(list)

    employee_receiving = forms.ChoiceField(choices=CHOICES, label='Przyjmujacy')
    employee_service = forms.ChoiceField(choices=CHOICES, label='Serwisant')


class AddTaskClientDataForm(forms.Form):
    # PROBA UZYCIA JAKO VALUE WEWNATRZ FORMULARZA EDYCJI - UZUPELNIONYCH POL - OSTATECZNIE UZYTO TEMPLATE'OW
    # def __init__(self, *args, **kwargs):
    #     self.id = kwargs.pop('id')
    #     super(AddTaskClientDataForm, self).__init__(*args, **kwargs)

    client_name = forms.CharField(max_length=128, label='Imie')
    client_surname = forms.CharField(max_length=128, label='Nazwisko')
    client_phone = forms.IntegerField(label='Tel')
    client_mail = forms.CharField(max_length=128, label='Mail')


class AddTaskBicycleDetailsForm(forms.Form):
    bicycle_name = forms.CharField(max_length=128, label='Model roweru')
    bicycle_year = forms.IntegerField(label='Rok')


class AddTaskDefectsForm(forms.Form):
    defects = Defects.objects.all()

    list = []
    for defect in defects:
        list.append((defect.id, defect))

    DEFECTS_CHOICES = tuple(list)

    defect = forms.MultipleChoiceField(choices=DEFECTS_CHOICES, label='Usterki',
                                       widget=forms.SelectMultiple(attrs={'size': 10}))


class AddTaskPartsForm(forms.Form):
    parts = Parts.objects.all()

    list = []
    for part in parts:
        list.append((part.id, part))

    PARTS_CHOICES = tuple(list)

    part = forms.MultipleChoiceField(choices=PARTS_CHOICES, label='Czesci do wymiany',
                                     widget=forms.SelectMultiple(attrs={'size': 10}))


class AddTaskAdditionalInfoForm(forms.Form):
    priority = forms.BooleanField(label='Priorytet')
    reclamation = forms.BooleanField(label='Reklamacja')
    payment_in_advance = forms.IntegerField(label='Zaliczka')
    notes = forms.CharField(label='Notatki', widget=forms.Textarea)


class AddTaskEstimatedPriceForm(forms.Form):
    # PROBLEM Z PRZYWOLANIEM SESJI W WIDOKU FORMS
    # t = Tasks.objects.last()
    # if t.priority:
    #     priority_price = 100
    # else:
    #     priority_price = 0
    #
    # p = TasksParts.objects.filter(task_id=t.id)
    # parts_price = 0
    # for part in p:
    #     parts_price += Parts.objects.get(id=part.part_id).average_price
    #
    # d = TasksDefects.objects.filter(task_id=t.id)
    # defects_price = 0
    # for defect in d:
    #     defects_price += Defects.objects.get(id=defect.defect_id).average_price
    #
    # if t.estimated_time:
    #     worktime_price = 60 * t.estimated_time.seconds / 3600
    # else:
    #     worktime_price = 0

    # calculated_estimated_price = priority_price + parts_price + defects_price + worktime_price
    calculated_estimated_price = 0

    estimated_price = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': f"{calculated_estimated_price}"}))
    estimated_time = forms.DurationField(widget=forms.TimeInput(attrs={'format': '%H:%M', 'type': 'time'}),
                                         label='Szacowany czas naprawy')
    photo = forms.ImageField(label='Zdjecie')
