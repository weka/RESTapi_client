# swagger_client.DefaultNetworkApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_default_network**](DefaultNetworkApi.md#get_default_network) | **GET** /defaultNet | Get default network
[**reset_default_network**](DefaultNetworkApi.md#reset_default_network) | **DELETE** /defaultNet | Reset default network
[**set_default_network**](DefaultNetworkApi.md#set_default_network) | **POST** /defaultNet | Set default network
[**update_default_network**](DefaultNetworkApi.md#update_default_network) | **PUT** /defaultNet | Update default network

# **get_default_network**
> InlineResponse2006 get_default_network()

Get default network

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultNetworkApi(swagger_client.ApiClient(configuration))

try:
    # Get default network
    api_response = api_instance.get_default_network()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultNetworkApi->get_default_network: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_default_network**
> InlineResponse200 reset_default_network()

Reset default network

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultNetworkApi(swagger_client.ApiClient(configuration))

try:
    # Reset default network
    api_response = api_instance.reset_default_network()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultNetworkApi->reset_default_network: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_default_network**
> InlineResponse200 set_default_network(body)

Set default network

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultNetworkApi(swagger_client.ApiClient(configuration))
body = swagger_client.DefaultNet() # DefaultNet | 

try:
    # Set default network
    api_response = api_instance.set_default_network(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultNetworkApi->set_default_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DefaultNet**](DefaultNet.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_default_network**
> InlineResponse200 update_default_network(body)

Update default network

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultNetworkApi(swagger_client.ApiClient(configuration))
body = swagger_client.DefaultNet() # DefaultNet | 

try:
    # Update default network
    api_response = api_instance.update_default_network(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultNetworkApi->update_default_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DefaultNet**](DefaultNet.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

