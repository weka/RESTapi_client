# swagger_client.StatsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_real_time_stats**](StatsApi.md#get_real_time_stats) | **GET** /stats/realtime | Get real time stats
[**get_stats**](StatsApi.md#get_stats) | **GET** /stats | Get stats
[**get_stats_description**](StatsApi.md#get_stats_description) | **GET** /stats/description | Get stats description
[**get_stats_disk_usage**](StatsApi.md#get_stats_disk_usage) | **GET** /stats/retention | Get stats retention and estimated disk usage
[**get_stats_retention**](StatsApi.md#get_stats_retention) | **POST** /stats/retention | Set stats retention

# **get_real_time_stats**
> InlineResponse20076 get_real_time_stats()

Get real time stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.StatsApi(swagger_client.ApiClient(configuration))

try:
    # Get real time stats
    api_response = api_instance.get_real_time_stats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_real_time_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20076**](InlineResponse20076.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats**
> InlineResponse20074 get_stats(start_time=start_time, end_time=end_time, interval=interval, category=category, stat=stat, resolution_secs=resolution_secs, accumulated=accumulated, per_node=per_node, node_uids=node_uids, param_param_key=param_param_key, no_zeroes=no_zeroes, show_internal=show_internal)

Get stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.StatsApi(swagger_client.ApiClient(configuration))
start_time = 'start_time_example' # str |  (optional)
end_time = 'end_time_example' # str |  (optional)
interval = 'interval_example' # str |  (optional)
category = ['category_example'] # list[str] | array of categories (optional)
stat = ['stat_example'] # list[str] |  (optional)
resolution_secs = 1.2 # float |  (optional)
accumulated = true # bool |  (optional)
per_node = true # bool |  (optional)
node_uids = ['node_uids_example'] # list[str] |  (optional)
param_param_key = ['param_param_key_example'] # list[str] |  (optional)
no_zeroes = true # bool |  (optional)
show_internal = true # bool |  (optional)

try:
    # Get stats
    api_response = api_instance.get_stats(start_time=start_time, end_time=end_time, interval=interval, category=category, stat=stat, resolution_secs=resolution_secs, accumulated=accumulated, per_node=per_node, node_uids=node_uids, param_param_key=param_param_key, no_zeroes=no_zeroes, show_internal=show_internal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **str**|  | [optional] 
 **end_time** | **str**|  | [optional] 
 **interval** | **str**|  | [optional] 
 **category** | [**list[str]**](str.md)| array of categories | [optional] 
 **stat** | [**list[str]**](str.md)|  | [optional] 
 **resolution_secs** | **float**|  | [optional] 
 **accumulated** | **bool**|  | [optional] 
 **per_node** | **bool**|  | [optional] 
 **node_uids** | [**list[str]**](str.md)|  | [optional] 
 **param_param_key** | [**list[str]**](str.md)|  | [optional] 
 **no_zeroes** | **bool**|  | [optional] 
 **show_internal** | **bool**|  | [optional] 

### Return type

[**InlineResponse20074**](InlineResponse20074.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats_description**
> InlineResponse20075 get_stats_description()

Get stats description

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.StatsApi(swagger_client.ApiClient(configuration))

try:
    # Get stats description
    api_response = api_instance.get_stats_description()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_stats_description: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20075**](InlineResponse20075.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats_disk_usage**
> InlineResponse20077 get_stats_disk_usage(retention_duration=retention_duration)

Get stats retention and estimated disk usage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.StatsApi(swagger_client.ApiClient(configuration))
retention_duration = 'retention_duration_example' # str | Duration (format - 1 minute 2 seconds, options - weeks, days, hours, minutes, seconds) (optional)

try:
    # Get stats retention and estimated disk usage
    api_response = api_instance.get_stats_disk_usage(retention_duration=retention_duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_stats_disk_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retention_duration** | **str**| Duration (format - 1 minute 2 seconds, options - weeks, days, hours, minutes, seconds) | [optional] 

### Return type

[**InlineResponse20077**](InlineResponse20077.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats_retention**
> InlineResponse20077 get_stats_retention(body=body)

Set stats retention

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.StatsApi(swagger_client.ApiClient(configuration))
body = swagger_client.StatsRetentionBody() # StatsRetentionBody |  (optional)

try:
    # Set stats retention
    api_response = api_instance.get_stats_retention(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_stats_retention: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatsRetentionBody**](StatsRetentionBody.md)|  | [optional] 

### Return type

[**InlineResponse20077**](InlineResponse20077.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

