from behave import *
import requests
import pdb


api_url = None
api_end_points = {}
request_headers = {}
request_body = {}
response_code = {}
response_text = {}

#Background step
@given("the user sets the CICD API url")
def rest_api_url(context):
    global api_url
    api_url = 'https://3.128.91.93/api/Language'
    api_end_points['GET_URL'] = api_url

#Common step
@given("the user set HEADER request content type as '{header_content}'")
def req_header(context, header_content):
    request_headers['Content-Type'] = header_content

#POST operation steps
@when("the user sets the request body value as '{value}'")
def post_req_data(context, value):
    api_end_points['POST_URL'] = api_url+"?value="+value


@when("the user sends the POST request")
def send_post(context):
    response = requests.post(url=api_end_points['POST_URL'], verify=False, headers=request_headers)
    response_code['POST_RESP_CODE'] = response.status_code
    response_text['POST_RESP_TEXT'] = response.text


@then("the user gets the POST response status code as {status}")
def post_result(context, status):
    assert response_code['POST_RESP_CODE'] is int(status), "The response code is "+str(response_code['POST_RESP_CODE'])+". Should be "+status


@then("the POST response text should include '{resp_text}'")
def post_text(context, resp_text):
    assert resp_text in response_text['POST_RESP_TEXT'], "The response code is "+str(response_code['POST_RESP_TEXT'])+". Should be "+resp_text


#GET operation steps
@when("the user sends the GET request")
def get_req(context):
    response = requests.get(url=api_end_points['GET_URL'], verify=False, headers=request_headers)
    response_code['GET_RESP_CODE'] = response.status_code


@then("the user gets the GET response status code  as {status}")
def result(context, status):
    assert response_code['GET_RESP_CODE'] is int(status), "The response code is "+str(response_code['GET_RESP_CODE'])+". Should be "+status

#PUT operation steps
@when("the user sets the request body to update 'Python' value as '{updated_val}'")
def update_value(context, updated_val):
    api_end_points['PUT_URL'] = api_url + "/3?value=" + updated_val


@when("the user sends the PUT request")
def send_put(context):
    response = requests.put(url=api_end_points['PUT_URL'], verify=False, headers=request_headers)
    response_code['PUT_RESP_CODE'] = response.status_code
    response_text['PUT_RESP_TEXT'] = response.text


@then("the user gets the PUT response status code as {status}")
def put_resp(context, status):
    assert response_code['PUT_RESP_CODE'] is int(status), "The response code is " + str(response_code['PUT_RESP_CODE']) + ". Should be " + status


@then("the PUT response text should be '{resp_text}'")
def put_resp_text(context, resp_text):
    assert response_text['PUT_RESP_TEXT'] == resp_text, "The response code is " + str(response_code['PUT_RESP_TEXT']) + ". Should be " + resp_text

#Delete operation steps
@when("the user sets the request url to delete the 'PHP' data")
def data_to_delete(context):
    api_end_points['DELETE_URL'] = api_url + "/3"


@when("the user sends the DELETE request")
def send_put(context):
    response = requests.put(url=api_end_points['DELETE_URL'], verify=False, headers=request_headers)
    response_code['DELETE_RESP_CODE'] = response.status_code
    response_text['DELETE_RESP_TEXT'] = response.text


@then("the user gets the DELETE response status code as {status}")
def put_resp(context, status):
    assert response_code['DELETE_RESP_CODE'] is int(status), "The response code is " + str(response_code['DELETE_RESP_CODE']) + ". Should be " + status


@then("the DELETE response text should be '{resp_text}'")
def put_resp_text(context, resp_text):
    assert response_text['DELETE_RESP_TEXT'] == resp_text, "The response code is " + str(response_code['DELETE_RESP_TEXT']) + ". Should be " + resp_text