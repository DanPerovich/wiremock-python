import pytest
import requests

from wiremock.constants import Config
from wiremock.client import *

basePath = 'https://python.wiremockapi.cloud'

@pytest.fixture # (1)
def wiremock_setup():
    Config.base_url = basePath + "/__admin" # (2)
    Mappings.create_mapping(
        Mapping(
            request=MappingRequest(method=HttpMethods.GET, url="/hello"),
            response=MappingResponse(status=200, body="hello from WireMock Cloud"),
            persistent=False,
        )
    ) # (3)      

def test_get_hello_world(wiremock_setup): # (4)
    response = requests.get(basePath + "/hello")

    assert response.status_code == 200
    assert response.content == b"hello from WireMock Cloud"

""" def test_get_hello_world_fail(wiremock_server): # (5)
    response = requests.get(basePath + "/helloworld")

    assert response.status_code == 200
    assert response.content == b"hello from WireMock Cloud" """