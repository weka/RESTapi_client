# swagger_client.HealthApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_health**](HealthApi.md#get_api_health) | **GET** /healthcheck | Check if API is alive
[**get_ui_health**](HealthApi.md#get_ui_health) | **GET** /ui/healthcheck | Check if UI is alive

# **get_api_health**
> str get_api_health()

Check if API is alive

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HealthApi(swagger_client.ApiClient(configuration))

try:
    # Check if API is alive
    api_response = api_instance.get_api_health()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->get_api_health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ui_health**
> str get_ui_health()

Check if UI is alive

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HealthApi(swagger_client.ApiClient(configuration))

try:
    # Check if UI is alive
    api_response = api_instance.get_ui_health()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->get_ui_health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

