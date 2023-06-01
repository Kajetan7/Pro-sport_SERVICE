from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse
from add_task.models import *


@pytest.mark.django_db
def test_tasks_list(user, tasks):
    client = Client()
    client.force_login(user)
    url = reverse('calendar_menu')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['tasks'].count() == len(tasks)
    for t in tasks:
        assert t in response.context['tasks']


@pytest.mark.django_db
def test_add_task_1_post(tasks, user, employees):
    client = Client()
    client.force_login(user)
    url = reverse('add_task_1')
    data = {
        'employee_receiving': employees[0].id,
        'employee_service': employees[1].id,
        'client_name': 'John',
        'client_surname': 'Smith',
        'client_phone': '123456789',
        'client_mail': 'j@s.com'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url.startswith(reverse('add_task_2'))


@pytest.mark.django_db
def test_add_task_2_post(user, parts, defects):
    client = Client()
    client.force_login(user)
    url = reverse('add_task_2')
    data = {
        'bicycle_name': 'fast one',
        'bicycle_year': '2000',
        'defects': [f'{defects[0].id}', f'{defects[1].id}'],
        'parts': [f'{parts[0].id}', f'{parts[1].id}']
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url.startswith(reverse('add_task_3'))
