from django.shortcuts import render
from django.views import View


class MainMenuView(View):

    def get(self, request):
        return render(request, 'menu/menu.html')

