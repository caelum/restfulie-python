from urllib2 import urlopen
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

@Given(r'the resource content is "(.*)"')
def and_the_resource_content_is_group1(group1):
    pass

@When(r'I request this resource as raw')
def when_i_request_this_resource_as_raw():
    ftc.raw_resource = Restfulie.at(ftc.uri).raw().get()

@Then(r'the response code is "(\d+)"')
def then_check_status_code(code):
    ftc.raw_resource.response.code |should| equal_to(int(code))

@Then(r'the response body is "(.*)"')
def and_the_response_body_is_group1(body):
    ftc.raw_resource.response.body |should| equal_to(body)

