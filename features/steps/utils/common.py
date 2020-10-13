import re, pdb, requests

api_end_points = {}
request_headers = {}
request_body = {}
response_code = {}
response_text = {}

api_url = 'https://3.128.91.93/api/Language'
header = 'application/json'

#Deleting the resource in end of the scenario execution by using below method
def delete_resource(context, response_text):
    index = re.findall(r'\d+',response_text)
    api_end_points['DELETE_URL'] = api_end_points['GET_URL'] + "/" + index[0]
    response = requests.delete(url=api_end_points['DELETE_URL'], verify=False, headers=request_headers)
    assert response.status_code is int(202), "The response code is " + str(response.status_code) + ". Should be 202"