# swagger_client.EventsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_events**](EventsApi.md#get_events) | **GET** /events | Get events
[**get_events_description**](EventsApi.md#get_events_description) | **GET** /events/describe | Get events description
[**get_local_events**](EventsApi.md#get_local_events) | **GET** /events/local | Get events from the targeted host for the API call

# **get_events**
> InlineResponse2009 get_events(num_results=num_results, start_time=start_time, end_time=end_time, severity=severity, type_list=type_list, category_list=category_list, sort_order=sort_order, show_internal=show_internal, next_token=next_token)

Get events

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.EventsApi(wekarestapi.ApiClient(configuration))
num_results = 1.2 # float |  (optional)
start_time = 'start_time_example' # str |  (optional)
end_time = 'end_time_example' # str |  (optional)
severity = 'severity_example' # str |  (optional)
type_list = ['type_list_example'] # list[str] |  (optional)
category_list = ['category_list_example'] # list[str] |  (optional)
sort_order = 'sort_order_example' # str |  (optional)
show_internal = true # bool |  (optional)
next_token = 'next_token_example' # str |  (optional)

try:
    # Get events
    api_response = api_instance.get_events(num_results=num_results, start_time=start_time, end_time=end_time, severity=severity, type_list=type_list, category_list=category_list, sort_order=sort_order, show_internal=show_internal, next_token=next_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_results** | **float**|  | [optional] 
 **start_time** | **str**|  | [optional] 
 **end_time** | **str**|  | [optional] 
 **severity** | **str**|  | [optional] 
 **type_list** | [**list[str]**](str.md)|  | [optional] 
 **category_list** | [**list[str]**](str.md)|  | [optional] 
 **sort_order** | **str**|  | [optional] 
 **show_internal** | **bool**|  | [optional] 
 **next_token** | **str**|  | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_description**
> InlineResponse20010 get_events_description(type=type, category=category, show_internal=show_internal)

Get events description

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.EventsApi(wekarestapi.ApiClient(configuration))
type = ['type_example'] # list[str] | list of categories (optional)
category = ['category_example'] # list[str] | list of categories (optional)
show_internal = true # bool |  (optional)

try:
    # Get events description
    api_response = api_instance.get_events_description(type=type, category=category, show_internal=show_internal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_events_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**list[str]**](str.md)| list of categories | [optional] 
 **category** | [**list[str]**](str.md)| list of categories | [optional] 
 **show_internal** | **bool**|  | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_local_events**
> InlineResponse20011 get_local_events(start_time=start_time, end_time=end_time, stem_mode=stem_mode, show_internal=show_internal, next_token=next_token)

Get events from the targeted host for the API call

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.EventsApi(wekarestapi.ApiClient(configuration))
start_time = 'start_time_example' # str |  (optional)
end_time = 'end_time_example' # str |  (optional)
stem_mode = true # bool |  (optional)
show_internal = true # bool |  (optional)
next_token = 'next_token_example' # str |  (optional)

try:
    # Get events from the targeted host for the API call
    api_response = api_instance.get_local_events(start_time=start_time, end_time=end_time, stem_mode=stem_mode, show_internal=show_internal, next_token=next_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_local_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **str**|  | [optional] 
 **end_time** | **str**|  | [optional] 
 **stem_mode** | **bool**|  | [optional] 
 **show_internal** | **bool**|  | [optional] 
 **next_token** | **str**|  | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

