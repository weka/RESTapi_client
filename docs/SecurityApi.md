# swagger_client.SecurityApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_login_banner**](SecurityApi.md#disable_login_banner) | **POST** /security/banner/disable | Disable login banner
[**enable_login_banner**](SecurityApi.md#enable_login_banner) | **POST** /security/banner/enable | Enable login banner
[**get_login_banner**](SecurityApi.md#get_login_banner) | **GET** /security/banner | Get the login banner
[**get_tokens_expiry**](SecurityApi.md#get_tokens_expiry) | **GET** /security/defaultTokensExpiry | Get tokens default expiry time
[**get_tokens_expiry_deprecated**](SecurityApi.md#get_tokens_expiry_deprecated) | **GET** /security/tokensExpiry | Get tokens default expiry time
[**set_ca_cert**](SecurityApi.md#set_ca_cert) | **PUT** /security/caCert | Set a CA-Cert for the cluster (Vault)
[**set_login_banner**](SecurityApi.md#set_login_banner) | **PUT** /security/banner | Set the login banner
[**show_ca_cert**](SecurityApi.md#show_ca_cert) | **GET** /security/caCert | Show the CA-Cert for the cluster (Vault)
[**unset_ca_cert**](SecurityApi.md#unset_ca_cert) | **DELETE** /security/caCert | Unset a CA-Cert for the cluster (Vault)

# **disable_login_banner**
> InlineResponse200 disable_login_banner()

Disable login banner

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
    # Disable login banner
    api_response = api_instance.disable_login_banner()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->disable_login_banner: %s\n" % e)
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

# **enable_login_banner**
> InlineResponse200 enable_login_banner()

Enable login banner

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
    # Enable login banner
    api_response = api_instance.enable_login_banner()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->enable_login_banner: %s\n" % e)
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

# **get_login_banner**
> InlineResponse20070 get_login_banner()

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

[**InlineResponse20070**](InlineResponse20070.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens_expiry**
> InlineResponse20069 get_tokens_expiry()

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

[**InlineResponse20069**](InlineResponse20069.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens_expiry_deprecated**
> InlineResponse20069 get_tokens_expiry_deprecated()

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
    api_response = api_instance.get_tokens_expiry_deprecated()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_tokens_expiry_deprecated: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20069**](InlineResponse20069.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_ca_cert**
> InlineResponse200 set_ca_cert(body=body)

Set a CA-Cert for the cluster (Vault)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SecurityApi(swagger_client.ApiClient(configuration))
body = swagger_client.SecurityCaCertBody() # SecurityCaCertBody |  (optional)

try:
    # Set a CA-Cert for the cluster (Vault)
    api_response = api_instance.set_ca_cert(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->set_ca_cert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecurityCaCertBody**](SecurityCaCertBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **show_ca_cert**
> InlineResponse20071 show_ca_cert()

Show the CA-Cert for the cluster (Vault)

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
    # Show the CA-Cert for the cluster (Vault)
    api_response = api_instance.show_ca_cert()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->show_ca_cert: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20071**](InlineResponse20071.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_ca_cert**
> InlineResponse200 unset_ca_cert()

Unset a CA-Cert for the cluster (Vault)

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
    # Unset a CA-Cert for the cluster (Vault)
    api_response = api_instance.unset_ca_cert()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->unset_ca_cert: %s\n" % e)
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

