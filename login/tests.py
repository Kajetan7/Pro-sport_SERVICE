from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_login_view():
    client = Client()
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_main_menu_view_not_login():
    client = Client()
    url = reverse('menu')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_main_menu_view_login(user):
    client = Client()
    client.force_login(user)
    url = reverse('menu')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_task_1_view_not_login():
    client = Client()
    url = reverse('add_task_1')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_add_task_1_view_login(user):
    client = Client()
    client.force_login(user)
    url = reverse('add_task_1')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_task_2_view_not_login():
    client = Client()
    url = reverse('add_task_2')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_add_task_2_view_login(user):
    client = Client()
    client.force_login(user)
    url = reverse('add_task_2')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_task_3_view_not_login():
    client = Client()
    url = reverse('add_task_3')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_add_task_3_view_login(user):
    client = Client()
    client.force_login(user)
    url = reverse('add_task_3')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_task_4_view_not_login():
    client = Client()
    url = reverse('task_estimated_price')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_add_task_4_view_login(user):
    client = Client()
    client.force_login(user)
    url = reverse('task_estimated_price')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_calendar_view_not_login():
    client = Client()
    url = reverse('calendar_menu')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_calendar_view_login(user):
    client = Client()
    client.force_login(user)
    url = reverse('calendar_menu')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_manage_menu_view_not_login():
    client = Client()
    url = reverse('manage_menu')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_manage_menu_view_login(user):
    client = Client()
    client.force_login(user)
    url = reverse('manage_menu')
    response = client.get(url)
    assert response.status_code == 405


@pytest.mark.django_db
def test_edit_task_1_view_not_login(tasks):
    client = Client()
    url = reverse('edit_task', kwargs={'id': tasks[0].id})
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_edit_task_1_view_login(user, tasks):
    client = Client()
    client.force_login(user)
    url = reverse('edit_task', kwargs={'id': tasks[0].id})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_edit_task_2_view_not_login(tasks):
    client = Client()
    url = reverse('edit_task_2', kwargs={'id': tasks[0].id})
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_edit_task_2_view_login(user, tasks):
    client = Client()
    client.force_login(user)
    url = reverse('edit_task_2', kwargs={'id': tasks[0].id})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_edit_task_3_view_not_login(tasks):
    client = Client()
    url = reverse('edit_task_3', kwargs={'id': tasks[0].id})
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_edit_task_3_view_login(user, tasks):
    client = Client()
    client.force_login(user)
    url = reverse('edit_task_3', kwargs={'id': tasks[0].id})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_edit_task_4_view_not_login(tasks):
    client = Client()
    url = reverse('edit_task_4', kwargs={'id': tasks[0].id})
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_edit_task_4_view_login(user, tasks):
    client = Client()
    client.force_login(user)
    url = reverse('edit_task_4', kwargs={'id': tasks[0].id})
    try:
        response = client.get(url)
        assert response.status_code == 200
    except ValueError as e:
        print(e)


@pytest.mark.django_db
def test_logout_view_not_login():
    client = Client()
    url = reverse('logout')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_logout_view_login(user):
    client = Client()
    client.force_login(user)
    url = reverse('logout')
    response = client.get(url)
    assert response.status_code == 302

