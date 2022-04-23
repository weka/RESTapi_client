from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint



###################################################
config = wekarestapi.Configuration()
config.host = "https://zweka01:14000/api/v2"
config.verify_ssl = False
config.access_token = None

# create an instance of the API class
api_client = wekarestapi.ApiClient(config)
api_instance = wekarestapi.LoginApi(api_client)

body = wekarestapi.LoginBody(username="admin", password="Weka.io123", org="root") # LoginBody |

try:
    # login to system
    api_response = api_instance.login(body)
    pprint(api_response)
    config.access_token = api_response.data.access_token
except ApiException as e:
    print("Exception when calling LoginApi->login: %s\n" % e)

print("##########################################################################################")
alertsapi_instance = wekarestapi.AlertsApi(api_client)

try:
    # get alerts
    api_response = alertsapi_instance.get_alerts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_alerts: %s\n" % e)

print("##########################################################################################")
eventsapi_instance = wekarestapi.EventsApi(api_client)
try:
    # get events
    api_response = eventsapi_instance.get_events()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_alerts: %s\n" % e)

print("##########################################################################################")
#eventsapi_instance = wekarestapi.EventsApi(api_client)
try:
    # get events
    api_response = wekarestapi.MachinesApi(api_client).get_machines()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->get_alerts: %s\n" % e)

print("run complete")