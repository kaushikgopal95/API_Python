import requests
from behave import *
from utilities.configurations import *
from features.environment import *


# Scenario: Validate to check the current UTC time
@given('Base url is provided')
def steps(context):
    context.baseurl = getconfig()['API']['baseurl']


@when('The slug value is passed and UTC time request is hit')
def steps(context):
    context.url = context.baseurl + getconfig()['API']['currentdate']
    context.response = requests.request('GET', context.url)


@then('Current date and time is displayed in UTC timezone')
def steps(context):
    assert context.response.status_code == 200, "Response code received is : %s" % context.response.status_code
    response_body = context.response.text
    assert response_body == context.response.headers.get('date')


# Scenario: Validate to check if the timestamp entered is valid

@when('the parameters are passed and the request is hit')
def steps(context):
    context.url = context.baseurl + getconfig()['API']['valid_time']
    context.params = {'timestamp': '2022-10-10'}
    context.response = requests.request('GET', context.url, params=context.params)
    # print(context.response.url)
    # print(context.response)


@then('Date format is verified')
def steps(context):
    assert context.response.status_code == 200, "Response code received is : %s" % context.response.status_code
    response_body = context.response.json()
    print(response_body)
    assert response_body['valid'] == True


# Scenario: Validate to check if a timestamp is between the time period

@when('the start date and end date are passed as query parameters')
def steps(context):
    context.url = context.baseurl + getconfig()['API']['betweentimestamps']
    params = {'timestamp': '2017-10-10', 'start': '2017-10-10', 'end': '2019-10-10'}
    context.response = requests.get(context.url, params=params)
    # print(context.response.url)


@then('the timestamp is validated')
def steps(context):
    assert context.response.status_code == 200, "Response code received is : %s" % context.response.status_code
    response_body = context.response.json()
    # print(response_body)
    assert response_body['between'] == False
    response_time = context.response.elapsed.total_seconds()
    # print("Response time is " + str(response_time))
    assert response_time <= 3
