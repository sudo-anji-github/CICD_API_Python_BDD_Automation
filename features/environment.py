from steps.utils.common import api_url, api_end_points, request_headers, header, response_text, delete_resource


#Hooks methods for Behave
def before_scenario(context, scenario):
    api_end_points['GET_URL'] = api_url
    request_headers['Content-Type'] = header
    print("Before_all")


def after_scenario(context, scenario):
    if ('POST' in scenario.name) or ('PUT' in scenario.name) or ('GETDELETE' in scenario.name):
        delete_resource(context, response_text['RESP_TEXT'])
    else:
        pass
