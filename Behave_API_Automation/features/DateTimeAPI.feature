# Created by kaushik at 23/11/22
Feature: Date and Time API to validate formats

@UTC-time
  Scenario: Validate to check the current UTC time
    Given Base url is provided
    When The slug value is passed and UTC time request is hit
    Then Current date and time is displayed in UTC timezone

@time-format
  Scenario: Validate to check if the timestamp entered is valid
    Given Base url is provided
    When the parameters are passed and the request is hit
    Then Date format is verified

@between-time
  Scenario: Validate to check if a timestamp is between the time period
    Given Base url is provided
    When the start date and end date are passed as query parameters
    Then the timestamp is validated

