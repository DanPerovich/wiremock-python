from wiremock.constants import Config
from wiremock.client import *
from wiremock.server.server import WireMockServer
import requests

WireMockServer(jar_path='/Users/dan/Development/wiremock-python/lib/wiremock-standalone-3.4.1.jar')
basePath = 'http://localhost'

with WireMockServer() as wm:
    Config.base_url = basePath + ':{}/__admin/'.format(wm.port)
    
    mapping = Mapping(
        priority=100,
        request=MappingRequest(
            method=HttpMethods.GET,
            url='/hello'
        ),
        response=MappingResponse(
            status=200,
            body='hi from standalone wiremock'
        ),
        persistent=False,
    )

    mapping = Mappings.create_mapping(mapping=mapping)

    all_mappings = Mappings.retrieve_all_mappings()

    response = requests.get(basePath + ':{}/hello'.format(wm.port))
    print("%s:%s" % (response.status_code, response.text))