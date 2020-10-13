Feature: CICD API Testing using Python BDD framework

  Background:
	Given the user sets the CICD API url


  @test1
  Scenario: Perform POST operation
    Given the user set HEADER request content type as 'application/json'
    When the user sets the request body value as 'Python'
    And the user sends the POST request
    Then the user gets the POST response status code as 201
    And the POST response text should include 'Python'


  @test2
  Scenario: Perform GET operation
    Given the user set HEADER request content type as 'application/json'
    When the user sends the GET request
    Then the user gets the GET response status code  as 200

  @test3
  Scenario: Perform PUT operation
    Given the user set HEADER request content type as 'application/json'
    When the user sets the request body to update 'Python' value as 'PHP'
    And the user sends the PUT request
    Then the user gets the PUT response status code as 200
    And the PUT response text should be '"Record updated successfully"'

  @test4
  Scenario: Perform Delete operation
    Given the user set HEADER request content type as 'application/json'
    When the user sets the request url to delete the 'PHP' data
    And the user sends the DELETE request
    Then the user gets the DELETE response status code as 200
    And the DELETE response text should be '"Record deleted successfully"'
