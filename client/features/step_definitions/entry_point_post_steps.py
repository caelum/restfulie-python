from should_dsl import should
from freshen import *
from restfulie import Restfulie

@Given(r'there is an URL accepting posts at "(.*)"')
def given_there_is_an_url_accepting_posts_at(uri):
    ftc.uri = uri

@When(r'I post the following content as "(.*)"')
def when_i_post_the_following_content_as(content, content_type):
    Restfulie.at(ftc.uri).as_(content_type).post(content)

@When(r'I request the resource at "(.*)" as raw')
def then_i_request_the_resource_as_raw(uri):
    ftc.resource = Restfulie.at(uri).raw().get()

