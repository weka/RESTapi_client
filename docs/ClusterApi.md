# swagger_client.ClusterApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cluster_status**](ClusterApi.md#get_cluster_status) | **GET** /cluster | Get cluster status
[**update_cluster**](ClusterApi.md#update_cluster) | **PUT** /cluster | Update cluster

# **get_cluster_status**
> InlineResponse2008 get_cluster_status()

Get cluster status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClusterApi(swagger_client.ApiClient(configuration))

try:
    # Get cluster status
    api_response = api_instance.get_cluster_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster**
> InlineResponse200 update_cluster(body)

Update cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClusterApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClusterBody() # ClusterBody | 

try:
    # Update cluster
    api_response = api_instance.update_cluster(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->update_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterBody**](ClusterBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

