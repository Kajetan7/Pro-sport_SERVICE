import pytest
from django.contrib.auth.models import User


@pytest.fixture
def user():
    u = User.objects.create(username='qwe')
    return u