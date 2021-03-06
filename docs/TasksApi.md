# swagger_client.TasksApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_tasks**](TasksApi.md#abort_tasks) | **POST** /tasks/{uid}/abort | Abort task
[**get_tasks**](TasksApi.md#get_tasks) | **GET** /tasks | Get all cluster tasks
[**get_tasks_limit**](TasksApi.md#get_tasks_limit) | **GET** /tasks/limits | Get cluster tasks limit
[**pause_tasks**](TasksApi.md#pause_tasks) | **POST** /tasks/{uid}/pause | Pause task
[**resume_task**](TasksApi.md#resume_task) | **POST** /tasks/{uid}/resume | Resume task
[**set_tasks_limit**](TasksApi.md#set_tasks_limit) | **PUT** /tasks/limits | Set cluster tasks limit

# **abort_tasks**
> InlineResponse200 abort_tasks(uid)

Abort task

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.TasksApi(wekarestapi.ApiClient(configuration))
uid = 'uid_example' # str | Task uid

try:
    # Abort task
    api_response = api_instance.abort_tasks(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->abort_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Task uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> InlineResponse20078 get_tasks()

Get all cluster tasks

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.TasksApi(wekarestapi.ApiClient(configuration))

try:
    # Get all cluster tasks
    api_response = api_instance.get_tasks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_tasks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20078**](InlineResponse20078.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_limit**
> InlineResponse20079 get_tasks_limit()

Get cluster tasks limit

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.TasksApi(wekarestapi.ApiClient(configuration))

try:
    # Get cluster tasks limit
    api_response = api_instance.get_tasks_limit()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_tasks_limit: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20079**](InlineResponse20079.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_tasks**
> InlineResponse200 pause_tasks(uid)

Pause task

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.TasksApi(wekarestapi.ApiClient(configuration))
uid = 'uid_example' # str | Task uid

try:
    # Pause task
    api_response = api_instance.pause_tasks(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->pause_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Task uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_task**
> InlineResponse200 resume_task(uid)

Resume task

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.TasksApi(wekarestapi.ApiClient(configuration))
uid = 'uid_example' # str | Task uid

try:
    # Resume task
    api_response = api_instance.resume_task(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->resume_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Task uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_tasks_limit**
> InlineResponse200 set_tasks_limit(body)

Set cluster tasks limit

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.TasksApi(wekarestapi.ApiClient(configuration))
body = wekarestapi.TasksLimitsBody() # TasksLimitsBody | 

try:
    # Set cluster tasks limit
    api_response = api_instance.set_tasks_limit(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->set_tasks_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TasksLimitsBody**](TasksLimitsBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

