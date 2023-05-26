from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from add_task.models import *


class CalendarView(ListView):
    model = Tasks
    template_name = 'calendar_menu/calendar_main.html'
    context_object_name = 'tasks'
    paginate_by = 5
    queryset = Tasks.objects.all().order_by('priority')
