# swagger_client.DriveApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_drives**](DriveApi.md#activate_drives) | **POST** /drives/activate | Activate drives
[**deactivates_drives**](DriveApi.md#deactivates_drives) | **POST** /drives/deactivate | Deactivate drives
[**delete_drive**](DriveApi.md#delete_drive) | **DELETE** /drives/{uid} | Remove drive
[**get_drives**](DriveApi.md#get_drives) | **GET** /drives | Get drives list
[**get_single_drive**](DriveApi.md#get_single_drive) | **GET** /drives/{uid} | Get single drive
[**provision_drives**](DriveApi.md#provision_drives) | **POST** /drives | Provision drives

# **activate_drives**
> InlineResponse200 activate_drives(body=body)

Activate drives

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DriveApi(swagger_client.ApiClient(configuration))
body = swagger_client.DrivesActivateBody() # DrivesActivateBody |  (optional)

try:
    # Activate drives
    api_response = api_instance.activate_drives(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriveApi->activate_drives: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DrivesActivateBody**](DrivesActivateBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivates_drives**
> InlineResponse200 deactivates_drives(body=body)

Deactivate drives

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DriveApi(swagger_client.ApiClient(configuration))
body = swagger_client.DrivesDeactivateBody() # DrivesDeactivateBody |  (optional)

try:
    # Deactivate drives
    api_response = api_instance.deactivates_drives(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriveApi->deactivates_drives: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DrivesDeactivateBody**](DrivesDeactivateBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_drive**
> InlineResponse200 delete_drive(uid)

Remove drive

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DriveApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | Drive uid

try:
    # Remove drive
    api_response = api_instance.delete_drive(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriveApi->delete_drive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Drive uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_drives**
> InlineResponse2007 get_drives(show_removed=show_removed)

Get drives list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DriveApi(swagger_client.ApiClient(configuration))
show_removed = true # bool |  (optional)

try:
    # Get drives list
    api_response = api_instance.get_drives(show_removed=show_removed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriveApi->get_drives: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_removed** | **bool**|  | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_drive**
> InlineResponse2008 get_single_drive(uid)

Get single drive

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DriveApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | Drive uid

try:
    # Get single drive
    api_response = api_instance.get_single_drive(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriveApi->get_single_drive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Drive uid | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provision_drives**
> InlineResponse2008 provision_drives(body)

Provision drives

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DriveApi(swagger_client.ApiClient(configuration))
body = swagger_client.DrivesBody() # DrivesBody | 

try:
    # Provision drives
    api_response = api_instance.provision_drives(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriveApi->provision_drives: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DrivesBody**](DrivesBody.md)|  | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

