from behave import *
import requests, re
import pdb
from steps.utils.common import api_end_points, request_headers, request_body, response_text, response_code


#POST operation steps
@given("the user sets the request value as '{value}'")
def post_req_data(context, value):
    api_end_points['POST_URL'] = api_end_points['GET_URL']+"?value="+value


@when("the user sends the POST request")
def send_post(context):
    response = requests.post(url=api_end_points['POST_URL'], verify=False, headers=request_headers)
    response_code['POST_RESP_CODE'] = response.status_code
    response_text['RESP_TEXT'] = response.text


@then("the user gets the POST response status code as {status}")
def post_result(context, status):
    assert response_code['POST_RESP_CODE'] is int(status), "The response code is "+str(response_code['POST_RESP_CODE'])+". Should be "+status


@then("the POST response text should include '{resp_text}'")
def post_text(context, resp_text):
    assert resp_text in response_text['RESP_TEXT'], "The response code is "+str(response_code['RESP_TEXT'])+". Should be "+resp_text


#GET operation steps
@given("the user gather the GET request url")
def gather_url(context):
    api_end_points['GET_DATA_URL'] = api_end_points['GET_URL']


@when("the user sends the GET request")
def get_req(context):
    response = requests.get(url=api_end_points['GET_DATA_URL'], verify=False, headers=request_headers)
    response_code['GET_RESP_CODE'] = response.status_code
    response_text['GET_RESP_TEXT'] = response.text


@then("the user gets the GET response status code  as {status}")
def result(context, status):
    assert response_code['GET_RESP_CODE'] is int(status), "The response code is "+str(response_code['GET_RESP_CODE'])+". Should be "+status


@then("the response text should not be empty")
def resp_text(context):
    assert len(response_text['GET_RESP_TEXT']) > 0, "The POST response text is "+response_text['GET_RESP_TEXT']+". Should not be empty"


#PUT operation steps
@given("the user creates the resource with the data value as '{value}'")
def create(context, value):
    api_end_points['POST_URL'] = api_end_points['GET_URL'] + "?value=" + value
    response = requests.post(url=api_end_points['POST_URL'], verify=False, headers=request_headers)
    response_text['RESP_TEXT'] = response.text


@when("the user sets the request body to update 'Cucumber' value as '{updated_val}'")
def update(context, updated_val):
    index = re.findall(r'\d+', response_text['RESP_TEXT'])
    api_end_points['PUT_URL'] = api_end_points['GET_URL'] + "/"+index[0]+"?value=" + updated_val


@when("sends the PUT request to update resource")
def send_put(context):
    response = requests.put(url=api_end_points['PUT_URL'], verify=False, headers=request_headers)
    response_code['PUT_RESP_CODE'] = response.status_code
    response_text['RESP_TEXT'] = response.text


@then("the user gets the PUT response status code as {status}")
def put_resp(context, status):
    assert response_code['PUT_RESP_CODE'] is int(status), "The response code is " + str(response_code['PUT_RESP_CODE']) + ". Should be " + status


@then("the PUT response text should include '{resp_text}'")
def post_text(context, resp_text):
    assert resp_text in response_text['RESP_TEXT'], "The response code is "+str(response_code['RESP_TEXT'])+". Should be "+resp_text



#Delete operation steps
@when("the user sends the DELETE request to delete the created resource")
def delete_req(context):
    index = re.findall(r'\d+', response_text['RESP_TEXT'])
    api_end_points['DELETE_URL'] = api_end_points['GET_URL'] + "/" + index[0]
    response = requests.delete(url=api_end_points['DELETE_URL'], verify=False, headers=request_headers)
    response_code['DELETE_RESP_CODE'] = response.status_code
    response_text['DELETE_RESP_TEXT'] = response.text


@then("the user gets the DELETE response status code as {status}")
def delete_resp(context, status):
    assert response_code['DELETE_RESP_CODE'] is int(status), "The response code is " + str(response_code['DELETE_RESP_CODE']) + ". Should be " + status


@then("the DELETE response text should include '{resp_text}'")
def delete_resp(context, resp_text):
    assert resp_text in response_text['DELETE_RESP_TEXT'], "The response code is " + str(response_code['DELETE_RESP_TEXT']) + ". Should be " + resp_text

