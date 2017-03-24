# -*- coding: utf-8 -*-
import os
import tempfile
import pytest
from backend import backend


@pytest.fixture
def client(request):
    client = backend.app.test_client()
    return client


def test_main_endpoint(client):
    response = client.get('/')
    assert b'Hello anonymous!' in response.data


def test_main_endpoint_with_param(client):
    response = client.get('/?name=John')
    assert b'Hello John!' in response.data
