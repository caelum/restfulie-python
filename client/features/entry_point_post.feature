Using steps: 'step_definitions/entry_point_post_steps', 'step_definitions/entry_point_steps'

Feature: Entry point post

  Scenario: post as application/xml
    Given there is an URL accepting posts at "http://localhost:8081/set_content"
    When I post the following content as "application/xml":
    """
      some content
    """
    And I request the resource at "http://localhost:8081/myresource" as raw
    Then the response body is
    """
      some content
    """

