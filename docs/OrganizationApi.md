# swagger_client.OrganizationApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization**](OrganizationApi.md#create_organization) | **POST** /organizations | Create organization
[**delete_organization**](OrganizationApi.md#delete_organization) | **DELETE** /organizations/{uid} | Delete organization
[**get_multiple_org_exist**](OrganizationApi.md#get_multiple_org_exist) | **GET** /organizations/multipleOrgsExist | Get if multiple Organizations Exist
[**get_organization**](OrganizationApi.md#get_organization) | **GET** /organizations/{uid} | Get organization
[**get_organizations**](OrganizationApi.md#get_organizations) | **GET** /organizations | Get all organizations
[**set_organization_limit**](OrganizationApi.md#set_organization_limit) | **PUT** /organizations/{uid}/limits | Set organization capacity limits
[**update_organization**](OrganizationApi.md#update_organization) | **PUT** /organizations/{uid} | update organization

# **create_organization**
> InlineResponse20052 create_organization(body)

Create organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
body = swagger_client.OrganizationsBody() # OrganizationsBody | 

try:
    # Create organization
    api_response = api_instance.create_organization(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->create_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrganizationsBody**](OrganizationsBody.md)|  | 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization**
> InlineResponse200 delete_organization(uid)

Delete organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | organization uid

try:
    # Delete organization
    api_response = api_instance.delete_organization(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->delete_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| organization uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multiple_org_exist**
> InlineResponse20053 get_multiple_org_exist()

Get if multiple Organizations Exist

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))

try:
    # Get if multiple Organizations Exist
    api_response = api_instance.get_multiple_org_exist()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_multiple_org_exist: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization**
> InlineResponse20052 get_organization(uid)

Get organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | organization uid

try:
    # Get organization
    api_response = api_instance.get_organization(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| organization uid | 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations**
> InlineResponse20051 get_organizations()

Get all organizations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))

try:
    # Get all organizations
    api_response = api_instance.get_organizations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organizations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_organization_limit**
> InlineResponse20052 set_organization_limit(uid, body=body)

Set organization capacity limits

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | organization uid
body = swagger_client.UidLimitsBody() # UidLimitsBody |  (optional)

try:
    # Set organization capacity limits
    api_response = api_instance.set_organization_limit(uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->set_organization_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| organization uid | 
 **body** | [**UidLimitsBody**](UidLimitsBody.md)|  | [optional] 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization**
> InlineResponse20052 update_organization(uid, body=body)

update organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | organization uid
body = swagger_client.OrganizationsUidBody() # OrganizationsUidBody |  (optional)

try:
    # update organization
    api_response = api_instance.update_organization(uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->update_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| organization uid | 
 **body** | [**OrganizationsUidBody**](OrganizationsUidBody.md)|  | [optional] 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

