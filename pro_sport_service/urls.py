"""pro_sport_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from login import views as login_views
from menu import views as menu_views
from add_task import views as add_task_views
from calendar_menu import views as calendar_menu_views
from manage_menu import views as manage_menu_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_views.LoginView.as_view(), name='login'),
    path('menu/', menu_views.MainMenuView.as_view(), name='menu'),
    path('add_task/1/', add_task_views.AddTaskForm1View.as_view(), name='add_task_1'),
    path('add_task/2/', add_task_views.AddTaskForm2View.as_view(), name='add_task_2'),
    path('add_task/3/', add_task_views.AddTaskForm3View.as_view(), name='add_task_3'),
    path('add_task/4/', add_task_views.AddTaskEstimatedPriceView.as_view(), name='task_estimated_price'),
    path('calendar_menu/', calendar_menu_views.CalendarView.as_view(), name='calendar_menu'),
    path('manage_menu', manage_menu_views.ManageMenuView.as_view(), name='manage_menu'),
    path('logout/', login_views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
