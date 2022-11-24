import requests
from behave import *
from utilities.configurations import *
from features.environment import *


# GET Request ############################
@given('The base url is provided')
def step_impl(context):
    context.url = getconfig()['API']['baseurl'] + endpoints.getrequest


@when('Execute the get request')
def step_impl(context):
    context.response = requests.get(context.url)


@then('the response code should be 200')
def step_impl(context):
    assert context.response.status_code == 200, "Response code received is : %s" % context.response.status_code

    response_body = context.response.json()
    assert response_body["args"]["foo1"] == "bar1", "Assertion failed, expected response was \"bar1\" "
    assert response_body["args"]["foo2"] == "bar2", "Assertion failed, expected response was \"bar2\" "


# POST Request ##################################
@given('The base url is provided along with raw text as body')
def step_impl(context):
    context.url = endpoints.baseurl + endpoints.postrequest  # calling the variables using resource file instead of
    # config file
    context.payload = "This is expected to be sent back as part of response body."


@when('Execute the post request')
def step_impl(context):
    context.response = requests.request("POST", context.url, data=context.payload)


@then('The response code should be 200 for post')
def step_impl(context):
    # print(context.response.content)
    assert context.response.status_code == 200, "Response code received is : %s" % context.response.status_code
    response_body = context.response.json()
    assert response_body["data"] == context.payload
    response_time = context.response.elapsed.total_seconds()
    print("Response time is " + str(response_time))
    assert response_time <= 3


@given('The base url is provided along with form data as body')
def stem_impl(context):
    context.url = getconfig()['API']['baseurl'] + endpoints.postrequest
    context.payload = 'foo1=bar1&foo2=bar2'
    context.headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'sails.sid=s%3A0avAdrlBsIDc7WUbJxgdTjqkhmBNojKV.N6ga5oZwjGinNOX7PR7hvKTwec%2FOFrSpF2GkhNKvT6M'
    }


@when('Execute the post request for form data payload')
def step_impl(context):
    context.response = requests.post(context.url, data=context.payload, headers=context.headers)


@then('The status code should be "{statuscode:d}"')
def step_impl(context, statuscode):
    assert context.response.status_code == 200, "Response code received is : %s" % context.response.status_code
    response_body = context.response.json()
    assert response_body['form']['foo1'] == "bar1"
    assert response_body['form']['foo2'] == "bar2"
    assert response_body['url'] == context.url
    response_time = context.response.elapsed.total_seconds()
    print("Response time is " + str(response_time))
    assert response_time <= 4


# PUT Request ############################

@given('The base url is provided along with put slug')
def step_impl(context):
    context.url = endpoints.baseurl + endpoints.putrequest
    print(context.url)
    # calling the variables using resource file instead of
    # config file

    context.payload = "This is expected to be sent back as part of response body."


@when('Execute the put request')
def step_impl(context):
    context.response = requests.request("PUT", context.url, data=context.payload)


@then('The status code for PUT should be "{statuscode:d}"')
def step_impl(context, statuscode):
    # print(context.response.content)
    assert context.response.status_code == 200, "Response code received is : %s" % context.response.status_code
    response_body = context.response.json()
    assert response_body["data"] == context.payload
    response_time = context.response.elapsed.total_seconds()
    # print("Response time is " + str(response_time))
    assert response_time <= 4


# Patch Request ############################

@given('The base url is provided for patch request')
def step_impl(context):
    context.url = getconfig()['API']['baseurl'] + endpoints.patchrequest
    print(context.url)


@when('Execute the patch request')
def step_impl(context):
    context.response = requests.request("PATCH", context.url, data=endpoints.payload)


@then('The status code for Patch request should be "{statuscode:d}"')
def step_impl(context, statuscode):
    # print(context.response.content)
    assert context.response.status_code == 200, "Response code received is : %s" % context.response.status_code
    response_body = context.response.json()
    assert response_body["data"] == endpoints.payload
    assert response_body["url"] == context.url
    response_time = context.response.elapsed.total_seconds()
    print("Response time is " + str(response_time))
    assert response_time <= 3


# Delete Request ############################

@given('The base url is provided for delete request')
def step_impl(context):
    context.url = getconfig()['API']['baseurl'] + endpoints.deleterequest


@when('Execute the delete request')
def step_impl(context):
    context.response = requests.request("Delete", context.url, data=endpoints.payload)


@then('The status code for delete request should be "{statuscode:d}"')
def step_impl(context, statuscode):
    assert context.response.status_code == 200, "Response code received is : %s" % context.response.status_code
    response_body = context.response.json()
    assert response_body["data"] == endpoints.payload
    assert response_body["url"] == context.url
    response_time = context.response.elapsed.total_seconds()
    # print("Response time is " + str(response_time))
    assert response_time <= 4
