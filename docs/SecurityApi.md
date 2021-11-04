# swagger_client.SecurityApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_login_banner**](SecurityApi.md#get_login_banner) | **GET** /security/banner | Get the login banner
[**get_tokens_expiry**](SecurityApi.md#get_tokens_expiry) | **GET** /security/tokensExpiry | Get tokens default expiry time
[**set_login_banner**](SecurityApi.md#set_login_banner) | **PUT** /security/banner | Set the login banner

# **get_login_banner**
> InlineResponse20059 get_login_banner()

Get the login banner

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SecurityApi(swagger_client.ApiClient(configuration))

try:
    # Get the login banner
    api_response = api_instance.get_login_banner()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_login_banner: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens_expiry**
> InlineResponse20058 get_tokens_expiry()

Get tokens default expiry time

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SecurityApi(swagger_client.ApiClient(configuration))

try:
    # Get tokens default expiry time
    api_response = api_instance.get_tokens_expiry()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_tokens_expiry: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_login_banner**
> InlineResponse200 set_login_banner(body)

Set the login banner

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SecurityApi(swagger_client.ApiClient(configuration))
body = swagger_client.SecurityBannerBody() # SecurityBannerBody | 

try:
    # Set the login banner
    api_response = api_instance.set_login_banner(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->set_login_banner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecurityBannerBody**](SecurityBannerBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

