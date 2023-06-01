import pytest
from add_task.models import *
from django.contrib.auth.models import User


@pytest.fixture
def tasks():
    lst = []
    lst.append(Tasks.objects.create(bicycle_name='ABC 1'))
    lst.append(Tasks.objects.create(bicycle_name='ABC 2'))
    lst.append(Tasks.objects.create(bicycle_name='ABC 3'))
    return lst


@pytest.fixture
def user():
    u = User.objects.create(username='qwe')
    return u


@pytest.fixture
def employees():
    lst = []
    lst.append(Employees.objects.create(name='Andrzej', surname='Andrzejewski'))
    lst.append(Employees.objects.create(name='Bogdan', surname='Bogdanowski'))
    lst.append(Employees.objects.create(name='Cezary', surname='Cezarowicz'))
    return lst


@pytest.fixture
def defects():
    lst = []
    lst.append(Defects.objects.create(description='defect1', average_price=1))
    lst.append(Defects.objects.create(description='defect2', average_price=2))
    lst.append(Defects.objects.create(description='defect3', average_price=3))
    return lst


@pytest.fixture
def parts():
    lst = []
    lst.append(Parts.objects.create(description='part1', average_price=1))
    lst.append(Parts.objects.create(description='part2', average_price=2))
    lst.append(Parts.objects.create(description='part3', average_price=3))
    return lst


