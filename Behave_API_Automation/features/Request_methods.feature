# Created by kaushik at 11/11/22
Feature: Request Methods
  HTTP has multiple requests such as GET, PUT, POST, DELETE, PATCH, HEAD

  @get
  Scenario: GET Request
    Given The base url is provided
    When Execute the get request
    Then the response code should be 200


  @Postraw
  Scenario: POST Request with Raw text as payload
    Given The base url is provided along with raw text as body
    When  execute the post request
    Then  The response code should be 200 for post

  @postform
  Scenario: Post Request with Form data as payload
    Given The base url is provided along with form data as body
    When  Execute the post request for form data payload
    Then  The status code should be "200"

  @PUT
  Scenario: Put request
    Given the base url is provided along with put slug
    When Execute the put request
    Then  The status code for PUT should be "200"

  @PATCH
  Scenario: Patch Request
    Given The base url is provided for patch request
    When  Execute the patch request
    Then  The status code for Patch request should be "200"

   @Delete
  Scenario: Delete Request
    Given The base url is provided for delete request
    When  Execute the delete request
    Then  The status code for delete request should be "200"