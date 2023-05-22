from django.shortcuts import render
from django.views import View
from .forms import AddTaskForm1


class AddTaskForm1View(View):

    def get(self, request):
        form = AddTaskForm1()
        return render(request, 'add_task/add_task_base.html', {'form': form})
