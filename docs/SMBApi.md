# swagger_client.SMBApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_samba_domain**](SMBApi.md#add_samba_domain) | **POST** /smb/domains | Add trusted domain to smb
[**add_share_to_samba**](SMBApi.md#add_share_to_samba) | **POST** /smb/shares | add share to smb
[**add_user_to_samba**](SMBApi.md#add_user_to_samba) | **POST** /smb/users/{share_uid}/{user_type} | Add user to smb
[**clear_samba**](SMBApi.md#clear_samba) | **DELETE** /smb | Clear smb cluster info
[**delete_samba_active_directory**](SMBApi.md#delete_samba_active_directory) | **PUT** /smb/activeDirectory | Leave smb active directory
[**delete_samba_domain**](SMBApi.md#delete_samba_domain) | **DELETE** /smb/domains/{uid} | Delete smb domain
[**delete_samba_share**](SMBApi.md#delete_samba_share) | **DELETE** /smb/shares/{uid} | Delete smb share
[**delete_samba_user**](SMBApi.md#delete_samba_user) | **DELETE** /smb/users/{share_uid}/{user_type}/{user} | Delete smb user
[**get_samba**](SMBApi.md#get_samba) | **GET** /smb | Get smb cluster info
[**reset_samba_users**](SMBApi.md#reset_samba_users) | **DELETE** /smb/users/reset/{share_uid}/{user_type} | Reset smb users
[**set_samba**](SMBApi.md#set_samba) | **POST** /smb | Set smb cluster info
[**set_samba_active_directory**](SMBApi.md#set_samba_active_directory) | **POST** /smb/activeDirectory | Join smb active directory
[**set_samba_debug**](SMBApi.md#set_samba_debug) | **POST** /smb/debug | Set smb debug level
[**set_samba_domains**](SMBApi.md#set_samba_domains) | **GET** /smb/domains | Get smb trusted domains
[**set_samba_mount_options**](SMBApi.md#set_samba_mount_options) | **GET** /smb/mount | Get smb mount options
[**set_samba_shares**](SMBApi.md#set_samba_shares) | **GET** /smb/shares | Get smb shares
[**update_samba**](SMBApi.md#update_samba) | **PUT** /smb | Update smb cluster info
[**update_samba_share**](SMBApi.md#update_samba_share) | **PUT** /smb/shares/{uid} | Update smb share

# **add_samba_domain**
> InlineResponse20053 add_samba_domain(body=body)

Add trusted domain to smb

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SMBApi(swagger_client.ApiClient(configuration))
body = swagger_client.SmbDomainsBody() # SmbDomainsBody |  (optional)

try:
    # Add trusted domain to smb
    api_response = api_instance.add_samba_domain(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMBApi->add_samba_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmbDomainsBody**](SmbDomainsBody.md)|  | [optional] 

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_share_to_samba**
> InlineResponse20056 add_share_to_samba(body=body)

add share to smb

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SMBApi(swagger_client.ApiClient(configuration))
body = swagger_client.SmbSharesBody() # SmbSharesBody |  (optional)

try:
    # add share to smb
    api_response = api_instance.add_share_to_samba(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMBApi->add_share_to_samba: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmbSharesBody**](SmbSharesBody.md)|  | [optional] 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_to_samba**
> InlineResponse200 add_user_to_samba(share_uid, user_type, body=body)

Add user to smb

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SMBApi(swagger_client.ApiClient(configuration))
share_uid = 'share_uid_example' # str | Share uid
user_type = 'user_type_example' # str | read_only, read_write, valid, invalid
body = swagger_client.ShareUidUserTypeBody() # ShareUidUserTypeBody |  (optional)

try:
    # Add user to smb
    api_response = api_instance.add_user_to_samba(share_uid, user_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMBApi->add_user_to_samba: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_uid** | **str**| Share uid | 
 **user_type** | **str**| read_only, read_write, valid, invalid | 
 **body** | [**ShareUidUserTypeBody**](ShareUidUserTypeBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_samba**
> InlineResponse200 clear_samba()

Clear smb cluster info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SMBApi(swagger_client.ApiClient(configuration))

try:
    # Clear smb cluster info
    api_response = api_instance.clear_samba()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMBApi->clear_samba: %s\n" % e)
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

# **delete_samba_active_directory**
> InlineResponse20057 delete_samba_active_directory(body=body)

Leave smb active directory

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SMBApi(swagger_client.ApiClient(configuration))
body = swagger_client.SmbActiveDirectoryBody() # SmbActiveDirectoryBody |  (optional)

try:
    # Leave smb active directory
    api_response = api_instance.delete_samba_active_directory(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMBApi->delete_samba_active_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmbActiveDirectoryBody**](SmbActiveDirectoryBody.md)|  | [optional] 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_samba_domain**
> InlineResponse200 delete_samba_domain(uid)

Delete smb domain

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SMBApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | Domain uid

try:
    # Delete smb domain
    api_response = api_instance.delete_samba_domain(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMBApi->delete_samba_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Domain uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_samba_share**
> InlineResponse200 delete_samba_share(uid)

Delete smb share

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SMBApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | Share uid

try:
    # Delete smb share
    api_response = api_instance.delete_samba_share(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMBApi->delete_samba_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Share uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_samba_user**
> InlineResponse200 delete_samba_user(share_uid, user_type, user)

Delete smb user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SMBApi(swagger_client.ApiClient(configuration))
share_uid = 'share_uid_example' # str | Share uid
user_type = 'user_type_example' # str | read_only, read_write, valid, invalid
user = 'user_example' # str | 

try:
    # Delete smb user
    api_response = api_instance.delete_samba_user(share_uid, user_type, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMBApi->delete_samba_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_uid** | **str**| Share uid | 
 **user_type** | **str**| read_only, read_write, valid, invalid | 
 **user** | **str**|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_samba**
> InlineResponse20051 get_samba()

Get smb cluster info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SMBApi(swagger_client.ApiClient(configuration))

try:
    # Get smb cluster info
    api_response = api_instance.get_samba()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMBApi->get_samba: %s\n" % e)
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

# **reset_samba_users**
> InlineResponse200 reset_samba_users(share_uid, user_type)

Reset smb users

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SMBApi(swagger_client.ApiClient(configuration))
share_uid = 'share_uid_example' # str | Share uid
user_type = 'user_type_example' # str | read_only, read_write, valid, invalid

try:
    # Reset smb users
    api_response = api_instance.reset_samba_users(share_uid, user_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMBApi->reset_samba_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_uid** | **str**| Share uid | 
 **user_type** | **str**| read_only, read_write, valid, invalid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_samba**
> InlineResponse200 set_samba(body=body)

Set smb cluster info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SMBApi(swagger_client.ApiClient(configuration))
body = swagger_client.SmbBody1() # SmbBody1 |  (optional)

try:
    # Set smb cluster info
    api_response = api_instance.set_samba(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMBApi->set_samba: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmbBody1**](SmbBody1.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_samba_active_directory**
> object set_samba_active_directory(body=body)

Join smb active directory

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SMBApi(swagger_client.ApiClient(configuration))
body = swagger_client.SmbActiveDirectoryBody1() # SmbActiveDirectoryBody1 |  (optional)

try:
    # Join smb active directory
    api_response = api_instance.set_samba_active_directory(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMBApi->set_samba_active_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmbActiveDirectoryBody1**](SmbActiveDirectoryBody1.md)|  | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_samba_debug**
> InlineResponse200 set_samba_debug(body=body)

Set smb debug level

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SMBApi(swagger_client.ApiClient(configuration))
body = swagger_client.SmbDebugBody() # SmbDebugBody |  (optional)

try:
    # Set smb debug level
    api_response = api_instance.set_samba_debug(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMBApi->set_samba_debug: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmbDebugBody**](SmbDebugBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_samba_domains**
> InlineResponse20052 set_samba_domains()

Get smb trusted domains

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SMBApi(swagger_client.ApiClient(configuration))

try:
    # Get smb trusted domains
    api_response = api_instance.set_samba_domains()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMBApi->set_samba_domains: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_samba_mount_options**
> InlineResponse20054 set_samba_mount_options()

Get smb mount options

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SMBApi(swagger_client.ApiClient(configuration))

try:
    # Get smb mount options
    api_response = api_instance.set_samba_mount_options()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMBApi->set_samba_mount_options: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_samba_shares**
> InlineResponse20055 set_samba_shares()

Get smb shares

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SMBApi(swagger_client.ApiClient(configuration))

try:
    # Get smb shares
    api_response = api_instance.set_samba_shares()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMBApi->set_samba_shares: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_samba**
> InlineResponse200 update_samba(body=body)

Update smb cluster info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SMBApi(swagger_client.ApiClient(configuration))
body = swagger_client.SmbBody() # SmbBody |  (optional)

try:
    # Update smb cluster info
    api_response = api_instance.update_samba(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMBApi->update_samba: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmbBody**](SmbBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_samba_share**
> InlineResponse20056 update_samba_share(uid, body=body)

Update smb share

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SMBApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | share uid
body = swagger_client.SharesUidBody() # SharesUidBody |  (optional)

try:
    # Update smb share
    api_response = api_instance.update_samba_share(uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMBApi->update_samba_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| share uid | 
 **body** | [**SharesUidBody**](SharesUidBody.md)|  | [optional] 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

