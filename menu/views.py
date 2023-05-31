from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse


class MainMenuView(LoginRequiredMixin, View):
    """
    A Django view that renders the main menu page.
    """
    def get(self, request):
        return render(request, 'menu/menu.html')

