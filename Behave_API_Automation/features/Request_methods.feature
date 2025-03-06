Feature: HTTP Request Methods
This feature covers testing various HTTP request methods, including GET, POST, PUT, DELETE, PATCH, and HEAD, 
to ensure they function correctly and return expected responses.

  @get  
  Scenario: Successful GET Request  
    Given the base URL is available  
    When I send a GET request  
    Then the response status code should be 200  

  @Postraw  
  Scenario: Successful POST Request with Raw Text Payload  
    Given the base URL is available with raw text as the request body  
    When I send a POST request  
    Then the response status code should be 200  

  @postform  
  Scenario: Successful POST Request with Form Data  
    Given the base URL is available with form data as the request body  
    When I send a POST request with form data  
    Then the response status code should be 200  

  @PUT  
  Scenario: Successful PUT Request  
    Given the base URL is available with a specific resource identifier  
    When I send a PUT request  
    Then the response status code should be 200  

  @PATCH  
  Scenario: Successful PATCH Request  
    Given the base URL is available for a PATCH request  
    When I send a PATCH request  
    Then the response status code should be 200  

  @Delete  
  Scenario: Successful DELETE Request  
    Given the base URL is available for a DELETE request  
    When I send a DELETE request  
    Then the response status code should be 200  
