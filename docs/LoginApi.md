# swagger_client.LoginApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](LoginApi.md#login) | **POST** /login | login to system
[**refresh_token**](LoginApi.md#refresh_token) | **POST** /login/refresh | get authentication tokens using refresh token

# **login**
> InlineResponse20030 login(body)

login to system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.LoginApi(swagger_client.ApiClient(configuration))
body = swagger_client.LoginBody() # LoginBody | 

try:
    # login to system
    api_response = api_instance.login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginBody**](LoginBody.md)|  | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token**
> InlineResponse20030 refresh_token(body)

get authentication tokens using refresh token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.LoginApi(swagger_client.ApiClient(configuration))
body = swagger_client.LoginRefreshBody() # LoginRefreshBody | 

try:
    # get authentication tokens using refresh token
    api_response = api_instance.refresh_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginRefreshBody**](LoginRefreshBody.md)|  | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

