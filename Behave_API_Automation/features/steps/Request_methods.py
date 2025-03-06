import requests  # Importing the requests library to send HTTP requests
from behave import *  # Importing Behave step definitions for BDD testing
from utilities.configurations import *  # Importing configuration functions to retrieve API base URL
from features.environment import *  # Importing endpoint definitions

# GET Request ############################
@given('The base url is provided')
def set_base_url(context):
    # Fetching base URL from properties.ini and appending the GET request endpoint
    context.url = getconfig()['API']['baseurl'] + endpoints.getrequest

@when('Execute the get request')
def send_get_request(context):
    # Sending a GET request and storing the response in context
    context.response = requests.get(context.url)

@then('the response code should be 200')
def validate_get_response(context):
    # Asserting the response status code is 200 (OK)
    assert context.response.status_code == 200, "Response code received is : %s" % context.response.status_code
    
    # Parsing the JSON response and verifying expected query parameters
    response_body = context.response.json()
    assert response_body["args"]["foo1"] == "bar1", "Assertion failed, expected response was \"bar1\" "
    assert response_body["args"]["foo2"] == "bar2", "Assertion failed, expected response was \"bar2\" "


# POST Request ##################################
@given('The base url is provided along with raw text as body')
def set_post_url_and_payload(context):
    # Setting the URL using endpoints variables instead of the config file
    context.url = endpoints.baseurl + endpoints.postrequest
    
    # Defining the raw text payload to be sent in the request body
    context.payload = "This is expected to be sent back as part of response body."

@when('Execute the post request')
def send_post_request(context):
    # Sending a POST request with raw text payload
    context.response = requests.request("POST", context.url, data=context.payload)

@then('The response code should be 200 for post')
def validate_post_response(context):
    # Asserting the response status code is 200
    assert context.response.status_code == 200, "Response code received is : %s" % context.response.status_code
    
    # Validating the response body matches the sent payload
    response_body = context.response.json()
    assert response_body["data"] == context.payload
    
    # Checking the response time does not exceed 3 seconds
    response_time = context.response.elapsed.total_seconds()
    print("Response time is " + str(response_time))
    assert response_time <= 3


@given('The base url is provided along with form data as body')
def set_post_form_data(context):
    # Fetching base URL and setting the POST request endpoint
    context.url = getconfig()['API']['baseurl'] + endpoints.postrequest
    
    # Defining form data payload
    context.payload = 'foo1=bar1&foo2=bar2'
    
    # Setting headers to specify form-data content type
    context.headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'sails.sid=s%3A0avAdrlBsIDc7WUbJxgdTjqkhmBNojKV.N6ga5oZwjGinNOX7PR7hvKTwec%2FOFrSpF2GkhNKvT6M'
    }

@when('Execute the post request for form data payload')
def send_post_form_request(context):
    # Sending a POST request with form data and headers
    context.response = requests.post(context.url, data=context.payload, headers=context.headers)

@then('The status code should be "{statuscode:d}"')
def validate_post_form_response(context, statuscode):
    # Asserting the response status code
    assert context.response.status_code == 200, "Response code received is : %s" % context.response.status_code
    
    # Validating form data in the response body
    response_body = context.response.json()
    assert response_body['form']['foo1'] == "bar1"
    assert response_body['form']['foo2'] == "bar2"
    assert response_body['url'] == context.url
    
    # Checking the response time does not exceed 4 seconds
    response_time = context.response.elapsed.total_seconds()
    print("Response time is " + str(response_time))
    assert response_time <= 4


# PUT Request ############################
@given('The base url is provided along with put slug')
def set_put_url_and_payload(context):
    # Setting the PUT request URL
    context.url = endpoints.baseurl + endpoints.putrequest
    
    # Defining the payload for the PUT request
    context.payload = "This is expected to be sent back as part of response body."

@when('Execute the put request')
def send_put_request(context):
    # Sending a PUT request with the payload
    context.response = requests.request("PUT", context.url, data=context.payload)

@then('The status code for PUT should be "{statuscode:d}"')
def validate_put_response(context, statuscode):
    # Asserting the response status code
    assert context.response.status_code == 200, "Response code received is : %s" % context.response.status_code
    
    # Validating the response body
    response_body = context.response.json()
    assert response_body["data"] == context.payload
    
    # Ensuring response time does not exceed 4 seconds
    response_time = context.response.elapsed.total_seconds()
    assert response_time <= 4
