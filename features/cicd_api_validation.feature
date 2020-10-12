Feature: CICD_API Testing using Python BDD framework

  Background:
	Given the user set REST API url of CICD

  @test1
  Scenario: Perform GET operation
    Given the user sets the GET api end point
    When the user set HEADER request content type as 'application/json'
    And the user sends the GET request
    Then the user gets the GET response status code  as 200