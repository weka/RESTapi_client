# swagger_client.LDAPApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ldap**](LDAPApi.md#delete_ldap) | **DELETE** /ldap | Reset LDAP configuration
[**get_ldap**](LDAPApi.md#get_ldap) | **GET** /ldap | Get LDAP configuration
[**update_ldap**](LDAPApi.md#update_ldap) | **PUT** /ldap | Update LDAP configuration

# **delete_ldap**
> InlineResponse200 delete_ldap()

Reset LDAP configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.LDAPApi(swagger_client.ApiClient(configuration))

try:
    # Reset LDAP configuration
    api_response = api_instance.delete_ldap()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LDAPApi->delete_ldap: %s\n" % e)
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

# **get_ldap**
> InlineResponse20036 get_ldap()

Get LDAP configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.LDAPApi(swagger_client.ApiClient(configuration))

try:
    # Get LDAP configuration
    api_response = api_instance.get_ldap()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LDAPApi->get_ldap: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ldap**
> InlineResponse200 update_ldap(body=body)

Update LDAP configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.LDAPApi(swagger_client.ApiClient(configuration))
body = swagger_client.LdapBody() # LdapBody |  (optional)

try:
    # Update LDAP configuration
    api_response = api_instance.update_ldap(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LDAPApi->update_ldap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LdapBody**](LdapBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

