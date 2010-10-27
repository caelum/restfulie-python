Feature: Allow entry point resource retrieval

  Scenario: server is available
    Given there is a resource at "http://localhost:8081/myresource"
    And the resource content is "<item><name>Rich Rock Sunshine</name></item>"
    When I request this resource as raw
    Then the response code is "200"
    And the response body is "<item><name>Rich Rock Sunshine</name></item>"

  Scenario Outline: xml retrieval
    Given there is a resource at "http://localhost:8081/myresource"
    And the resource content-type is "<content-type>"
    And the resource content is "<items><item><name>product</name><price>2</price></item></items>"
    When I request this resource
    Then the resource #1 item name is "product"
    And the resource #1 item price is "2"
    Examples:
      | content-type    |
      | application/xml |
      | text/xml        |

  Scenario: json retrieval
    Given there is a resource at "http://localhost:8081/myresource"
    And the resource content-type is "application/json"
    And the resource content is "{"item": {"name": "product", "price": 2}}"
    When I request this resource
    Then the resource item name is "product"
    And the resource item price is "2"

