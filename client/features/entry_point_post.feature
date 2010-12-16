Feature: Entry point post

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

#  Scenario: received a redirect (201) from post
#    Given there is an URL accepting posts at "http://localhost:8081/set_content"
#    When I post "redirect_to http://localhost:8081/myresource" as "application/xml"
#    Then I should be redirected to "http://localhost:8081/myresource" by the post


Scenario: Follow 201 response location
    Given there is an URL accepting posts at "http://localhost:8081/set_content"
    And this URL responds "201" as status code
    And this URL responds "http://localhost:8081/myresource" as "Location" header
    And there is a resource at "http://localhost:8081/myresource"
    And the resource content is "<items><item><name>product</name><price>2</price></item></items>"
    When I post a dict containing "{'anything': {'here': 'does not matter'}}" as "application/xml"
    Then the resource #1 item name is "product"
    And the resource #1 item price is "2"

