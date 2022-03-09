# swagger_client.KMSApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_kms**](KMSApi.md#delete_kms) | **DELETE** /kms | Delete kms configuration
[**get_kms**](KMSApi.md#get_kms) | **GET** /kms | Get kms configuration
[**get_kms_type**](KMSApi.md#get_kms_type) | **GET** /kms/type | Get kms type
[**rewrap_kms_key**](KMSApi.md#rewrap_kms_key) | **POST** /kms/rewrap | Rewrap KMS key
[**set_kms**](KMSApi.md#set_kms) | **POST** /kms | Set kms vault configuration (base_url,master_key_name,token) or set kms kmip configuration (server_endpoint, key_uid, client_cert_pem, client_key_pem, ca_cert_pem) 

# **delete_kms**
> InlineResponse200 delete_kms(force_delete=force_delete)

Delete kms configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.KMSApi(swagger_client.ApiClient(configuration))
force_delete = true # bool |  (optional)

try:
    # Delete kms configuration
    api_response = api_instance.delete_kms(force_delete=force_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KMSApi->delete_kms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **force_delete** | **bool**|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kms**
> InlineResponse20036 get_kms()

Get kms configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.KMSApi(swagger_client.ApiClient(configuration))

try:
    # Get kms configuration
    api_response = api_instance.get_kms()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KMSApi->get_kms: %s\n" % e)
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

# **get_kms_type**
> InlineResponse20037 get_kms_type()

Get kms type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.KMSApi(swagger_client.ApiClient(configuration))

try:
    # Get kms type
    api_response = api_instance.get_kms_type()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KMSApi->get_kms_type: %s\n" % e)
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

# **rewrap_kms_key**
> rewrap_kms_key(body)

Rewrap KMS key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.KMSApi(swagger_client.ApiClient(configuration))
body = swagger_client.KmsRewrapBody() # KmsRewrapBody | 

try:
    # Rewrap KMS key
    api_instance.rewrap_kms_key(body)
except ApiException as e:
    print("Exception when calling KMSApi->rewrap_kms_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KmsRewrapBody**](KmsRewrapBody.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_kms**
> InlineResponse200 set_kms(body)

Set kms vault configuration (base_url,master_key_name,token) or set kms kmip configuration (server_endpoint, key_uid, client_cert_pem, client_key_pem, ca_cert_pem) 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.KMSApi(swagger_client.ApiClient(configuration))
body = swagger_client.KmsBody() # KmsBody | 

try:
    # Set kms vault configuration (base_url,master_key_name,token) or set kms kmip configuration (server_endpoint, key_uid, client_cert_pem, client_key_pem, ca_cert_pem) 
    api_response = api_instance.set_kms(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KMSApi->set_kms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KmsBody**](KmsBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

