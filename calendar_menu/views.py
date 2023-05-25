from django.shortcuts import render
from django.views import View
from add_task.models import *


class CalendarView(View):

    def get(self, request):
        tasks = Tasks.objects.all()
        clients = Clients.objects.all()
        defects = Defects.objects.all()
        parts = Parts.objects.all()
        context = {
            'tasks': tasks,
            'clients': clients,
            'defects': defects,
            'parts': parts
        }
        return render(request, 'calendar_menu/calendar_main.html', context)


