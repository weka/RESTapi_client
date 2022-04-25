from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint



###################################################
config = wekarestapi.Configuration(hostname="vweka01")

# create an instance of the API class
api_client = wekarestapi.ApiClient(config)

try:
    # login to system
    api_response = wekarestapi.LoginApi(api_client).login(
        wekarestapi.LoginBody(username="admin", password="Weka.io123", org="root"))
#    pprint(api_response)
    config.auth_tokens = api_response.data
except ApiException as e:
    print("Exception when calling LoginApi->login: %s\n" % e)

print("##########################################################################################")

try:
    # get alerts
    api_response = wekarestapi.AlertsApi(api_client).get_alerts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_alerts: %s\n" % e)

print("##########################################################################################")
try:
    # get events
    api_response = wekarestapi.EventsApi(api_client).get_events()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_events: %s\n" % e)

print("##########################################################################################")
try:
    # get machines
    api_response = wekarestapi.MachinesApi(api_client).get_machines()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->get_machines: %s\n" % e)

print("##########################################################################################")
try:
    # get cluster status
    api_response = wekarestapi.ClusterApi(api_client).get_cluster_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_status: %s\n" % e)

print("run complete")