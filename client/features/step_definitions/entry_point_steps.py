import urllib
import urllib2
from should_dsl import should
from freshen import *
from restfulie import Restfulie
from fake_server import start_server, stop_server

@Before
def start(arg):
    start_server()

@After
def stop(arg):
    stop_server()

@Given(r'there is a resource at "(.*)"')
def given_there_is_a_resource_at_group1(uri):
    ftc.uri = uri

@Given(r'the resource content is')
def and_the_resource_content_is(content):
    data = urllib.urlencode({'content': content})
    urllib.urlopen('http://localhost:8081/set_content', data)

@Given(r'the resource content-type is "(.*)"')
def set_resource_content_type_to(content_type):
    data = urllib.urlencode({'content_type': content_type})
    urllib.urlopen('http://localhost:8081/set_content_type', data)

@When(r'I request this resource as raw')
def when_i_request_this_resource_as_raw():
    ftc.resource = Restfulie.at(ftc.uri).raw().get()

@When(r'I request this resource$')
def when_i_request_this_resource():
    ftc.resource = Restfulie.at(ftc.uri).get()

@Then(r'the response code is "(\d+)"')
def then_check_status_code(code):
    ftc.resource.response.code |should| equal_to(int(code))

@Then(r'the response body is')
def and_the_response_body_is(content):
    ftc.resource.response.body |should| equal_to(content)

@Then(r'the resource item name is "(.*)"')
def resource_item_name_is(name):
    ftc.resource.item.name |should| equal_to(name)

@Then(r'the resource item price is "(.*)"')
def resource_item_price_is(price):
    ftc.resource.item.price |should| equal_to(int(price))

