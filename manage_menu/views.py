from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class ManageMenuView(LoginRequiredMixin, View):
    """
    A Django view that renders the manage menu page.
    """
    pass
