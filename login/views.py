from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm
from django.contrib.auth import login, logout


class LoginView(View):
    """
    A Django view for handling login functionality:
    - rendering the login form
    - processing form submissions
    """
    def get(self, request):
        form = LoginForm()
        return render(request, 'login/index.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            if user is not None:
                login(request, user)
            return redirect('menu')
        return render(request, 'login/index.html', {'form': form})


class LogoutView(View):
    """
    A Django view for handling logout functionality:
    - logs out the currently authenticated user
    - redirects them to the login page
    """
    def get(self, request):
        logout(request)
        return redirect('login')
