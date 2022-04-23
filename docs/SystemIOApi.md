# swagger_client.SystemIOApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**start_io**](SystemIOApi.md#start_io) | **POST** /io/start | Start system IO
[**stop_io**](SystemIOApi.md#stop_io) | **POST** /io/stop | Stop system IO

# **start_io**
> InlineResponse20032 start_io()

Start system IO

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.SystemIOApi(wekarestapi.ApiClient(configuration))

try:
    # Start system IO
    api_response = api_instance.start_io()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemIOApi->start_io: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_io**
> InlineResponse20033 stop_io(body=body)

Stop system IO

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.SystemIOApi(wekarestapi.ApiClient(configuration))
body = wekarestapi.IoStopBody() # IoStopBody |  (optional)

try:
    # Stop system IO
    api_response = api_instance.stop_io(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemIOApi->stop_io: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IoStopBody**](IoStopBody.md)|  | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

