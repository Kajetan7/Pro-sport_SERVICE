from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from add_task.models import *
from django.contrib.auth.mixins import LoginRequiredMixin


class CalendarView(LoginRequiredMixin, ListView):
    """
    A Django view for:
    - displaying a calendar, with the requirement of the user being authenticated
    - uses the Tasks model to retrieve tasks data in paginated view
    - the queryset retrieves all tasks and orders them by priority
    """
    model = Tasks
    template_name = 'calendar_menu/calendar_main.html'
    context_object_name = 'tasks'
    paginate_by = 5
    queryset = Tasks.objects.all().order_by('priority')
