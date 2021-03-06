# swagger_client.ClusterApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster**](ClusterApi.md#create_cluster) | **POST** /cluster | Create cluster
[**get_cluster_status**](ClusterApi.md#get_cluster_status) | **GET** /cluster | Get cluster status
[**update_cluster**](ClusterApi.md#update_cluster) | **PUT** /cluster | Update cluster

# **create_cluster**
> InlineResponse2005 create_cluster(body)

Create cluster

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.ClusterApi(wekarestapi.ApiClient(configuration))
body = wekarestapi.ClusterBody1() # ClusterBody1 | 

try:
    # Create cluster
    api_response = api_instance.create_cluster(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->create_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterBody1**](ClusterBody1.md)|  | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_status**
> InlineResponse2004 get_cluster_status()

Get cluster status

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.ClusterApi(wekarestapi.ApiClient(configuration))

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

[**InlineResponse2004**](InlineResponse2004.md)

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
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.ClusterApi(wekarestapi.ApiClient(configuration))
body = wekarestapi.ClusterBody() # ClusterBody | 

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

