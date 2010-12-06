import urllib
import urllib2
from should_dsl import should
from lettuce import *
from restfulie import Restfulie

@step(r'Given there is a resource at "(.*)"')
def given_there_is_a_resource_at_group1(step, uri):
    world.uri = uri

@step(r'And the resource content is "(.*)"')
def and_the_resource_content_is(step, content):
    data = urllib.urlencode({'content': content})
    urllib.urlopen('http://localhost:8081/set_content', data)

@step(r'[Given|And] the resource content-type is "(.*)"')
def set_resource_content_type_to(step, content_type):
    data = urllib.urlencode({'content_type': content_type})
    urllib.urlopen('http://localhost:8081/set_content_type', data)

@step(r'When I request this resource as raw')
def when_i_request_this_resource_as_raw(step):
    world.resource = Restfulie.at(world.uri).raw().get()

@step(r'When I request this resource$')
def when_i_request_this_resource(step):
    world.resource = Restfulie.at(world.uri).get()

@step(r'Then the response code is "(\d+)"')
def then_check_status_code(step, code):
    world.resource.response.code |should| equal_to(int(code))

@step(r'[And|Then] the response body is "(.*)"$')
def and_the_response_body_is(step, content):
    world.resource.response.body |should| equal_to(content)

@step(r'Then the resource \#([0-9]+) item name is "(.*)"')
def resource_item_name_is(step, index, name):
    world.resource.items[int(index) - 1].name |should| equal_to(name)

@step(r'And the resource \#([0-9]+) item price is "(.*)"')
def resource_item_price_is(step, index, price):
    world.resource.items[int(index) - 1].price |should| equal_to(int(price))

@step(r'Then the resource item name is "(.*)"')
def resource_item_name_is(step, name):
    world.resource.item.name |should| equal_to(name)

@step(r'And the resource item price is "(.*)"')
def resource_item_price_is(step, price):
    world.resource.item.price |should| equal_to(int(price))

