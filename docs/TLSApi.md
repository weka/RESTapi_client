# swagger_client.TLSApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_tls**](TLSApi.md#disable_tls) | **DELETE** /tls | Disable tls
[**enable_tls**](TLSApi.md#enable_tls) | **POST** /tls | Enable TLS
[**get_tls**](TLSApi.md#get_tls) | **GET** /tls | Get TLS status

# **disable_tls**
> InlineResponse200 disable_tls()

Disable tls

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.TLSApi(wekarestapi.ApiClient(configuration))

try:
    # Disable tls
    api_response = api_instance.disable_tls()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TLSApi->disable_tls: %s\n" % e)
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

# **enable_tls**
> InlineResponse200 enable_tls(body=body)

Enable TLS

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.TLSApi(wekarestapi.ApiClient(configuration))
body = wekarestapi.TlsBody() # TlsBody |  (optional)

try:
    # Enable TLS
    api_response = api_instance.enable_tls(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TLSApi->enable_tls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TlsBody**](TlsBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tls**
> InlineResponse20080 get_tls()

Get TLS status

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.TLSApi(wekarestapi.ApiClient(configuration))

try:
    # Get TLS status
    api_response = api_instance.get_tls()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TLSApi->get_tls: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20080**](InlineResponse20080.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

