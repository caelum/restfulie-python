Feature: Entry point post

# Support
#
# Restfulie.at('uri').as('application/xml').post(some_object)
#
# Where some_object is a hash
# In this case, serialize this hash as an xml and send it to the server
#
# Note that in order to decide the marshalling algorithm, it should use the
# global media type control (hash) that maps a string to a driver
# (marshaller+unmarshaller)

  Scenario: post as application/xml
    Given there is an URL accepting posts at "http://localhost:8081/set_content"
    When I post a dict containing "{'item': {'description': 'Black Lantern t-shirt'}}" as "application/xml"
    And I request the resource at "http://localhost:8081/myresource" as raw
    Then the response body is "<item><description>Black Lantern t-shirt</description></item>"

  Scenario: post as application/json
    Given there is an URL accepting posts at "http://localhost:8081/set_content"
    When I post a dict containing "{'content':'some content'}" as "application/json"
    And I request the resource at "http://localhost:8081/myresource" as raw
    Then the response body is "{'content':'some content'}" as json

