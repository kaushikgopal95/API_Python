import requests
import configparser
import json


class endpoints:
    baseurl = 'https://postman-echo.com'
    getrequest = '/get?foo1=bar1&foo2=bar2'
    postrequest = '/post'
    putrequest = '/put'
    patchrequest = '/patch'
    payload = "This is expected to be sent back as part of response body."
    deleterequest = '/delete'