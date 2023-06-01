import pytest
from django.contrib.auth.models import User
from add_task.models import *

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