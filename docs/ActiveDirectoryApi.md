# swagger_client.ActiveDirectoryApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_ldap_active_directory**](ActiveDirectoryApi.md#update_ldap_active_directory) | **PUT** /activeDirectory | Update active directory

# **update_ldap_active_directory**
> InlineResponse200 update_ldap_active_directory(body)

Update active directory

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.ActiveDirectoryApi(wekarestapi.ApiClient(configuration))
body = wekarestapi.ActiveDirectoryBody() # ActiveDirectoryBody | 

try:
    # Update active directory
    api_response = api_instance.update_ldap_active_directory(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActiveDirectoryApi->update_ldap_active_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActiveDirectoryBody**](ActiveDirectoryBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

