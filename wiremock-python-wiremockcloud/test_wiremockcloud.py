from wiremock.constants import Config
from wiremock.client import *
import requests

basePath = 'https://python.wiremockapi.cloud'

Config.base_url = basePath + '/__admin/'

mapping = Mapping(
    priority=100,
    request=MappingRequest(
        method=HttpMethods.GET,
        url='/hello'
    ),
    response=MappingResponse(
        status=200,
        body='hi from WireMock Cloud'
    ),
    persistent=True,
)

mapping = Mappings.create_mapping(mapping=mapping)

#all_mappings = Mappings.retrieve_all_mappings()

response = requests.get(basePath + '/hello')
print("%s:%s" % (response.status_code, response.text))

mapping = Mappings.delete_all_mappings()