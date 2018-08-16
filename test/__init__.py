import pytest
from mixer.backend.django import mixer
from rest_framework.test import APIClient
from rest_framework import status
from _project import generate_token

pytestmark = pytest.mark.django_db

def get_api_url(url, version="v1"):
    return f"/api/{version}{url}"

def create_user(is_active):
    user = User.objects.filter(id=1).first()
    if user:
        user.is_active = is_active
        user.save()
        return user
    user = mixer.blend(User, id=1, is_active=is_active)
    user.set_password('123')
    user.save()
    return user

def get_token(is_active=True):
    user = create_user(is_active)
    data = {
        'email': user.email,
        'password': "123"
    }
    return generate_token(user), user

def get_api_client():
    token, user = get_token(is_active=True)

    client = APIClient(enforce_csrf_checks=True)
    client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
    return client