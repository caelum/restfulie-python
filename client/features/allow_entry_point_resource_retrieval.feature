Using steps: 'step_definitions/entry_point_steps'

Feature: Allow entry point resource retrieval

  Scenario: server is available
    Given there is a resource at "http://localhost:8081/myresource"
    And the resource content is "<item><name>Rich Rock Sunshine</name></item>"
    When I request this resource as raw
    Then the response code is "200"
    And the response body is "<item><name>Rich Rock Sunshine</name></item>"

