from urllib2 import urlopen
from should_dsl import should
from lettuce import step, world
from restfulie import Restfulie

@step(r'Given there is a resource at "(.*)"')
def given_there_is_a_resource_at_group1(step, uri):
    world.uri = uri

@step(r'And the resource content is "(.*)"')
def and_the_resource_content_is_group1(step, group1):
    pass

@step(r'When I request this resource as raw')
def when_i_request_this_resource_as_raw(step):
    world.raw_resource = Restfulie.at(world.uri).raw().get()

@step(r'Then the response code is "(\d+)"')
def then_check_status_code(step, code):
    world.raw_resource.response.code |should| equal_to(int(code))

@step(r'And the response body is "(.*)"')
def and_the_response_body_is_group1(step, body):
    world.raw_resource.response.body |should| equal_to(body)

