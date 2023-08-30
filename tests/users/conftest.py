import pytest
import requests

from config import SERV_URL


@pytest.fixture()
def get_users():
    response = requests.get(SERV_URL)
    return response