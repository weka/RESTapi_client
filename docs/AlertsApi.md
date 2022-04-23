# swagger_client.AlertsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alert_description**](AlertsApi.md#get_alert_description) | **GET** /alerts/description | Get alerts description
[**get_alerts**](AlertsApi.md#get_alerts) | **GET** /alerts | Get all alerts
[**get_alerts_types**](AlertsApi.md#get_alerts_types) | **GET** /alerts/types | Get alerts types
[**mute_alert_by_type**](AlertsApi.md#mute_alert_by_type) | **PUT** /alerts/{alert_type}/mute | Mute alerts by type
[**unmute_alert_by_type**](AlertsApi.md#unmute_alert_by_type) | **PUT** /alerts/{alert_type}/unmute | Unmute alerts by type

# **get_alert_description**
> InlineResponse2002 get_alert_description()

Get alerts description

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.AlertsApi(wekarestapi.ApiClient(configuration))

try:
    # Get alerts description
    api_response = api_instance.get_alert_description()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_alert_description: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts**
> InlineResponse2001 get_alerts()

Get all alerts

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.AlertsApi(wekarestapi.ApiClient(configuration))

try:
    # Get all alerts
    api_response = api_instance.get_alerts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_alerts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts_types**
> InlineResponse2003 get_alerts_types()

Get alerts types

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.AlertsApi(wekarestapi.ApiClient(configuration))

try:
    # Get alerts types
    api_response = api_instance.get_alerts_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_alerts_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mute_alert_by_type**
> InlineResponse200 mute_alert_by_type(body, alert_type)

Mute alerts by type

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.AlertsApi(wekarestapi.ApiClient(configuration))
body = wekarestapi.AlertTypeMuteBody() # AlertTypeMuteBody | 
alert_type = 'alert_type_example' # str | Alert type

try:
    # Mute alerts by type
    api_response = api_instance.mute_alert_by_type(body, alert_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->mute_alert_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertTypeMuteBody**](AlertTypeMuteBody.md)|  | 
 **alert_type** | **str**| Alert type | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unmute_alert_by_type**
> InlineResponse200 unmute_alert_by_type(alert_type)

Unmute alerts by type

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.AlertsApi(wekarestapi.ApiClient(configuration))
alert_type = 'alert_type_example' # str | Alert type

try:
    # Unmute alerts by type
    api_response = api_instance.unmute_alert_by_type(alert_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->unmute_alert_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_type** | **str**| Alert type | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

