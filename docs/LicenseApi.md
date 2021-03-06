# swagger_client.LicenseApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_license**](LicenseApi.md#get_license) | **GET** /license | Get license
[**reset_license**](LicenseApi.md#reset_license) | **DELETE** /license | Reset license
[**set_license**](LicenseApi.md#set_license) | **POST** /license | Set license

# **get_license**
> InlineResponse20037 get_license()

Get license

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.LicenseApi(wekarestapi.ApiClient(configuration))

try:
    # Get license
    api_response = api_instance.get_license()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_license**
> InlineResponse200 reset_license()

Reset license

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.LicenseApi(wekarestapi.ApiClient(configuration))

try:
    # Reset license
    api_response = api_instance.reset_license()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->reset_license: %s\n" % e)
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

# **set_license**
> InlineResponse200 set_license(body=body)

Set license

Classic license (license) or PAYG license (plan_id,secret_key,[url])

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.LicenseApi(wekarestapi.ApiClient(configuration))
body = wekarestapi.LicenseBody() # LicenseBody |  (optional)

try:
    # Set license
    api_response = api_instance.set_license(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->set_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LicenseBody**](LicenseBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

