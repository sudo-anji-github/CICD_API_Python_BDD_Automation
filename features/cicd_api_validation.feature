Feature: CI/CD API Testing Automation using Python BDD framework


  @test1
  Scenario: Perform POST operation to create resource
    Given the user sets the request value as 'Python'
    When the user sends the POST request
    Then the user gets the POST response status code as 201
    And the POST response text should include 'Python'


  @test2
  Scenario: Perform GET operation to get the specific resource
    Given the user creates the resource with the data value as 'Cucumber'
    When the user sends the GET request to get the specific resource
    Then the user gets the GET response status code as 200
    And the GET response text should include 'Cucumber' resource


  @test3
  Scenario: Perform GET operation to get the all resources
    Given the user gather the GET request url
    When the user sends the GET request
    Then the user gets the GET response status code as 200
    And the response text should not be empty


  @test4
  Scenario: Perform PUT operation to update the resource
    Given the user creates the resource with the data value as 'Cucucmber'
    When the user sets the request body to update 'Cucumber' value as 'Behave'
    And sends the PUT request to update resource
    Then the user gets the PUT response status code as 201
    And the PUT response text should include 'Behave'


  @test5
  Scenario: Perform Delete operation to delete the resource
    Given the user creates the resource with the data value as 'Cucucmber'
    When the user sends the DELETE request to delete the created resource
    Then the user gets the DELETE response status code as 202
    And the DELETE response text should include 'Cucucmber deleted successfully'
