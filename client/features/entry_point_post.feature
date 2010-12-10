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

  Scenario: received a redirect (201) from post
    Given there is an URL accepting posts at "http://localhost:8081/set_content"
    When I post "redirect_to http://localhost:8081/myresource" as "application/xml"
    Then I should be redirected to "http://localhost:8081/myresource" by the post

