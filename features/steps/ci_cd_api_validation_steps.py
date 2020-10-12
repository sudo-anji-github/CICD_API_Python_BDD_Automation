from behave import *
import requests

api_url = None
api_end_points = {}
request_headers = {}
request_body = {}
response_code = {}
response_text = {}


@given("the user set REST API url of CICD")
def rest_api_url(context):
    global api_url
    api_url = 'https://3.128.91.93/api/Language'


@given("the user sets the GET api end point")
def get_api_end_point(context):
    api_end_points['GET_URL'] = api_url


@when("the user set HEADER request content type as '{header_content}'")
def req_header(context, header_content):
    request_headers['Content-Type'] = header_content


@when("the user sends the GET request")
def get_req(context):
    response = requests.get(url=api_end_points['GET_URL'], verify=False, headers=request_headers)
    response_code['GET_RESP_CODE'] = response.status_code


@then("the user gets the GET response status code  as {status}")
def result(context, status):
    assert response_code['GET_RESP_CODE'] is int(status), "The response code is "+str(response_code['GET_RESP_CODE'])+". Should be "+status