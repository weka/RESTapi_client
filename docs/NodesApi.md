# swagger_client.NodesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_node**](NodesApi.md#get_node) | **GET** /nodes/{uid} | Get node
[**get_nodes**](NodesApi.md#get_nodes) | **GET** /nodes | Get all nodes

# **get_node**
> InlineResponse20034 get_node(uid)

Get node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NodesApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | Node uid

try:
    # Get node
    api_response = api_instance.get_node(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodesApi->get_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Node uid | 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes**
> InlineResponse20048 get_nodes()

Get all nodes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NodesApi(swagger_client.ApiClient(configuration))

try:
    # Get all nodes
    api_response = api_instance.get_nodes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodesApi->get_nodes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

