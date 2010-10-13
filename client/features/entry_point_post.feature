Feature: Entry point post

  Scenario: post as application/xml
    Given there is an URL accepting posts at "http://localhost:8081/set_content"
    When I post "some content" as "application/xml"
    And I request the resource at "http://localhost:8081/myresource" as raw
    Then the response body is "some content"

