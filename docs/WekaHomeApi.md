# swagger_client.WekaHomeApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_cloud**](WekaHomeApi.md#disable_cloud) | **POST** /wekaHome/disable | Disable cloud
[**enable_cloud**](WekaHomeApi.md#enable_cloud) | **POST** /wekaHome/enable | Enable cloud
[**get_cloud**](WekaHomeApi.md#get_cloud) | **GET** /wekaHome | Get cloud config
[**get_cloud_proxy**](WekaHomeApi.md#get_cloud_proxy) | **GET** /wekaHome/proxy | Get cloud proxy
[**get_cloud_upload_rate**](WekaHomeApi.md#get_cloud_upload_rate) | **GET** /wekaHome/uploadRate | Get cloud upload rate
[**get_cloud_url**](WekaHomeApi.md#get_cloud_url) | **GET** /wekaHome/url | Get cloud url
[**set_cloud_proxy**](WekaHomeApi.md#set_cloud_proxy) | **POST** /wekaHome/proxy | Set cloud proxy
[**update_cloud_upload_rate**](WekaHomeApi.md#update_cloud_upload_rate) | **PUT** /wekaHome/uploadRate | Update cloud upload rate

# **disable_cloud**
> InlineResponse200 disable_cloud()

Disable cloud

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WekaHomeApi(swagger_client.ApiClient(configuration))

try:
    # Disable cloud
    api_response = api_instance.disable_cloud()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WekaHomeApi->disable_cloud: %s\n" % e)
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

# **enable_cloud**
> InlineResponse200 enable_cloud(body)

Enable cloud

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WekaHomeApi(swagger_client.ApiClient(configuration))
body = swagger_client.WekaHomeEnableBody() # WekaHomeEnableBody | 

try:
    # Enable cloud
    api_response = api_instance.enable_cloud(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WekaHomeApi->enable_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WekaHomeEnableBody**](WekaHomeEnableBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud**
> InlineResponse20084 get_cloud()

Get cloud config

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WekaHomeApi(swagger_client.ApiClient(configuration))

try:
    # Get cloud config
    api_response = api_instance.get_cloud()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WekaHomeApi->get_cloud: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20084**](InlineResponse20084.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_proxy**
> InlineResponse20085 get_cloud_proxy()

Get cloud proxy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WekaHomeApi(swagger_client.ApiClient(configuration))

try:
    # Get cloud proxy
    api_response = api_instance.get_cloud_proxy()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WekaHomeApi->get_cloud_proxy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20085**](InlineResponse20085.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_upload_rate**
> InlineResponse20086 get_cloud_upload_rate()

Get cloud upload rate

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WekaHomeApi(swagger_client.ApiClient(configuration))

try:
    # Get cloud upload rate
    api_response = api_instance.get_cloud_upload_rate()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WekaHomeApi->get_cloud_upload_rate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20086**](InlineResponse20086.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_url**
> InlineResponse20087 get_cloud_url()

Get cloud url

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WekaHomeApi(swagger_client.ApiClient(configuration))

try:
    # Get cloud url
    api_response = api_instance.get_cloud_url()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WekaHomeApi->get_cloud_url: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20087**](InlineResponse20087.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_cloud_proxy**
> InlineResponse20085 set_cloud_proxy(body)

Set cloud proxy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WekaHomeApi(swagger_client.ApiClient(configuration))
body = swagger_client.WekaHomeProxyBody() # WekaHomeProxyBody | 

try:
    # Set cloud proxy
    api_response = api_instance.set_cloud_proxy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WekaHomeApi->set_cloud_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WekaHomeProxyBody**](WekaHomeProxyBody.md)|  | 

### Return type

[**InlineResponse20085**](InlineResponse20085.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_upload_rate**
> InlineResponse200 update_cloud_upload_rate(body)

Update cloud upload rate

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WekaHomeApi(swagger_client.ApiClient(configuration))
body = swagger_client.WekaHomeUploadRateBody() # WekaHomeUploadRateBody | 

try:
    # Update cloud upload rate
    api_response = api_instance.update_cloud_upload_rate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WekaHomeApi->update_cloud_upload_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WekaHomeUploadRateBody**](WekaHomeUploadRateBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

