# swagger_client.FailureDomainsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_failure_domains**](FailureDomainsApi.md#get_failure_domains) | **GET** /failureDomains | Get failure domains
[**get_single_failure_domain**](FailureDomainsApi.md#get_single_failure_domain) | **GET** /failureDomains/{uid} | Get single failure domain

# **get_failure_domains**
> InlineResponse20016 get_failure_domains(show_removed=show_removed)

Get failure domains

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FailureDomainsApi(swagger_client.ApiClient(configuration))
show_removed = true # bool |  (optional)

try:
    # Get failure domains
    api_response = api_instance.get_failure_domains(show_removed=show_removed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FailureDomainsApi->get_failure_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_removed** | **bool**|  | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_failure_domain**
> InlineResponse20017 get_single_failure_domain(uid)

Get single failure domain

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FailureDomainsApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | Domain uid

try:
    # Get single failure domain
    api_response = api_instance.get_single_failure_domain(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FailureDomainsApi->get_single_failure_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Domain uid | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

