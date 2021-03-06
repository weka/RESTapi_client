# swagger_client.S3Api

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_s3_policy**](S3Api.md#attach_s3_policy) | **POST** /s3/policies/attach | Attach an S3 IAM policy to a user
[**create_s3_bucket**](S3Api.md#create_s3_bucket) | **POST** /s3/buckets | Create an S3 bucket
[**create_s3_cluster**](S3Api.md#create_s3_cluster) | **POST** /s3 | Create S3 cluster
[**create_s3_policy**](S3Api.md#create_s3_policy) | **POST** /s3/policies | Create an S3 IAM policy
[**delete_s3_cluster**](S3Api.md#delete_s3_cluster) | **DELETE** /s3 | Delete S3 cluster
[**delete_s3_policy**](S3Api.md#delete_s3_policy) | **DELETE** /s3/policies/{policy} | Delete an S3 IAM policy
[**destroy_s3_bucket**](S3Api.md#destroy_s3_bucket) | **DELETE** /s3/buckets/{bucket} | Destroy an S3 bucket
[**detach_s3_policy**](S3Api.md#detach_s3_policy) | **POST** /s3/policies/detach | Detach a user&#x27;s policy
[**get_s3_bucket_disk_usage**](S3Api.md#get_s3_bucket_disk_usage) | **GET** /s3/buckets/{bucket}/diskUsage | Get the disk usage of an S3 bucket
[**get_s3_bucket_policy**](S3Api.md#get_s3_bucket_policy) | **GET** /s3/buckets/{bucket}/policy | Get the S3 bucket policy
[**get_s3_bucket_policy_json**](S3Api.md#get_s3_bucket_policy_json) | **GET** /s3/buckets/{bucket}/policyJson | Get the S3 bucket policy json
[**get_s3_buckets**](S3Api.md#get_s3_buckets) | **GET** /s3/buckets | Get S3 buckets list
[**get_s3_cluster**](S3Api.md#get_s3_cluster) | **GET** /s3 | Get S3 cluster info
[**get_s3_policies**](S3Api.md#get_s3_policies) | **GET** /s3/policies | Get S3 IAM policies list
[**get_s3_policy**](S3Api.md#get_s3_policy) | **GET** /s3/policies/{policy} | Get the details of an S3 IAM policy
[**gets3_containers_are_ready**](S3Api.md#gets3_containers_are_ready) | **GET** /s3/containersAreReady | Get S3 Hosts status
[**s3_create_lifecycle_rule**](S3Api.md#s3_create_lifecycle_rule) | **POST** /s3/buckets/{bucket}/lifecycle/rules | Create a new bucket lifecycle rule
[**s3_delete_all_lifecycle_rules**](S3Api.md#s3_delete_all_lifecycle_rules) | **DELETE** /s3/buckets/{bucket}/lifecycle/rules | Delete all lifecycle rules of a specific bucket
[**s3_delete_lifecycle_rule**](S3Api.md#s3_delete_lifecycle_rule) | **DELETE** /s3/buckets/{bucket}/lifecycle/rules/{rule} | Delete a bucket lifecycle rule
[**s3_list_all_lifecycle_rules**](S3Api.md#s3_list_all_lifecycle_rules) | **GET** /s3/buckets/{bucket}/lifecycle/rules | List all lifecycle rules of a specific bucket
[**s3_sts_create**](S3Api.md#s3_sts_create) | **POST** /s3/sts | Create an s3 sts token with an assumend role
[**set_s3_bucket_policy**](S3Api.md#set_s3_bucket_policy) | **PUT** /s3/buckets/{bucket}/policy | Set S3 bucket policy
[**set_s3_bucket_policy_json**](S3Api.md#set_s3_bucket_policy_json) | **PUT** /s3/buckets/{bucket}/policyJson | Set S3 bucket policy json
[**set_s3_bucket_quota**](S3Api.md#set_s3_bucket_quota) | **PUT** /s3/buckets/{bucket}/quota | Set S3 bucket quota
[**unset_s3_bucket_quota**](S3Api.md#unset_s3_bucket_quota) | **DELETE** /s3/buckets/{bucket}/quota | Unset S3 bucket quota
[**update_s3_cluster**](S3Api.md#update_s3_cluster) | **PUT** /s3 | Update S3 cluster

# **attach_s3_policy**
> InlineResponse200 attach_s3_policy(body)

Attach an S3 IAM policy to a user

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
body = wekarestapi.PoliciesAttachBody() # PoliciesAttachBody | 

try:
    # Attach an S3 IAM policy to a user
    api_response = api_instance.attach_s3_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->attach_s3_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PoliciesAttachBody**](PoliciesAttachBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_s3_bucket**
> InlineResponse200 create_s3_bucket(body)

Create an S3 bucket

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
body = wekarestapi.S3BucketsBody() # S3BucketsBody | 

try:
    # Create an S3 bucket
    api_response = api_instance.create_s3_bucket(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->create_s3_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**S3BucketsBody**](S3BucketsBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_s3_cluster**
> InlineResponse400 create_s3_cluster(body)

Create S3 cluster

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
body = wekarestapi.S3Body1() # S3Body1 | 

try:
    # Create S3 cluster
    api_response = api_instance.create_s3_cluster(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->create_s3_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**S3Body1**](S3Body1.md)|  | 

### Return type

[**InlineResponse400**](InlineResponse400.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_s3_policy**
> InlineResponse200 create_s3_policy(body)

Create an S3 IAM policy

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
body = wekarestapi.S3PoliciesBody() # S3PoliciesBody | 

try:
    # Create an S3 IAM policy
    api_response = api_instance.create_s3_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->create_s3_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**S3PoliciesBody**](S3PoliciesBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_s3_cluster**
> InlineResponse400 delete_s3_cluster(purge_config=purge_config)

Delete S3 cluster

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
purge_config = true # bool | Purge the existing configuraion by default (optional)

try:
    # Delete S3 cluster
    api_response = api_instance.delete_s3_cluster(purge_config=purge_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->delete_s3_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purge_config** | **bool**| Purge the existing configuraion by default | [optional] 

### Return type

[**InlineResponse400**](InlineResponse400.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_s3_policy**
> InlineResponse200 delete_s3_policy(policy)

Delete an S3 IAM policy

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
policy = 'policy_example' # str | policy name

try:
    # Delete an S3 IAM policy
    api_response = api_instance.delete_s3_policy(policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->delete_s3_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | **str**| policy name | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_s3_bucket**
> InlineResponse200 destroy_s3_bucket(bucket, unlink=unlink)

Destroy an S3 bucket

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
bucket = 'bucket_example' # str | bucket name
unlink = true # bool | unlinks the bucket, but leave the data directory in place (optional)

try:
    # Destroy an S3 bucket
    api_response = api_instance.destroy_s3_bucket(bucket, unlink=unlink)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->destroy_s3_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| bucket name | 
 **unlink** | **bool**| unlinks the bucket, but leave the data directory in place | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_s3_policy**
> InlineResponse200 detach_s3_policy(body)

Detach a user's policy

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
body = wekarestapi.PoliciesDetachBody() # PoliciesDetachBody | 

try:
    # Detach a user's policy
    api_response = api_instance.detach_s3_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->detach_s3_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PoliciesDetachBody**](PoliciesDetachBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_s3_bucket_disk_usage**
> InlineResponse200 get_s3_bucket_disk_usage(bucket)

Get the disk usage of an S3 bucket

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
bucket = 'bucket_example' # str | bucket name

try:
    # Get the disk usage of an S3 bucket
    api_response = api_instance.get_s3_bucket_disk_usage(bucket)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->get_s3_bucket_disk_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| bucket name | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_s3_bucket_policy**
> InlineResponse20058 get_s3_bucket_policy(bucket)

Get the S3 bucket policy

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
bucket = 'bucket_example' # str | bucket name

try:
    # Get the S3 bucket policy
    api_response = api_instance.get_s3_bucket_policy(bucket)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->get_s3_bucket_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| bucket name | 

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_s3_bucket_policy_json**
> InlineResponse20058 get_s3_bucket_policy_json(bucket)

Get the S3 bucket policy json

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
bucket = 'bucket_example' # str | bucket name

try:
    # Get the S3 bucket policy json
    api_response = api_instance.get_s3_bucket_policy_json(bucket)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->get_s3_bucket_policy_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| bucket name | 

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_s3_buckets**
> InlineResponse20055 get_s3_buckets()

Get S3 buckets list

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))

try:
    # Get S3 buckets list
    api_response = api_instance.get_s3_buckets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->get_s3_buckets: %s\n" % e)
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

# **get_s3_cluster**
> InlineResponse400 get_s3_cluster()

Get S3 cluster info

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))

try:
    # Get S3 cluster info
    api_response = api_instance.get_s3_cluster()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->get_s3_cluster: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse400**](InlineResponse400.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_s3_policies**
> InlineResponse200 get_s3_policies()

Get S3 IAM policies list

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))

try:
    # Get S3 IAM policies list
    api_response = api_instance.get_s3_policies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->get_s3_policies: %s\n" % e)
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

# **get_s3_policy**
> InlineResponse200 get_s3_policy(policy)

Get the details of an S3 IAM policy

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
policy = 'policy_example' # str | policy name

try:
    # Get the details of an S3 IAM policy
    api_response = api_instance.get_s3_policy(policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->get_s3_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | **str**| policy name | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gets3_containers_are_ready**
> InlineResponse20059 gets3_containers_are_ready()

Get S3 Hosts status

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))

try:
    # Get S3 Hosts status
    api_response = api_instance.gets3_containers_are_ready()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->gets3_containers_are_ready: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s3_create_lifecycle_rule**
> InlineResponse20056 s3_create_lifecycle_rule(body, bucket)

Create a new bucket lifecycle rule

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
body = wekarestapi.LifecycleRulesBody() # LifecycleRulesBody | 
bucket = 'bucket_example' # str | bucket name

try:
    # Create a new bucket lifecycle rule
    api_response = api_instance.s3_create_lifecycle_rule(body, bucket)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->s3_create_lifecycle_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LifecycleRulesBody**](LifecycleRulesBody.md)|  | 
 **bucket** | **str**| bucket name | 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s3_delete_all_lifecycle_rules**
> InlineResponse20057 s3_delete_all_lifecycle_rules(bucket)

Delete all lifecycle rules of a specific bucket

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
bucket = 'bucket_example' # str | bucket name

try:
    # Delete all lifecycle rules of a specific bucket
    api_response = api_instance.s3_delete_all_lifecycle_rules(bucket)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->s3_delete_all_lifecycle_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| bucket name | 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s3_delete_lifecycle_rule**
> InlineResponse20057 s3_delete_lifecycle_rule(bucket, rule)

Delete a bucket lifecycle rule

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
bucket = 'bucket_example' # str | bucket name
rule = 'rule_example' # str | rule ID

try:
    # Delete a bucket lifecycle rule
    api_response = api_instance.s3_delete_lifecycle_rule(bucket, rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->s3_delete_lifecycle_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| bucket name | 
 **rule** | **str**| rule ID | 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s3_list_all_lifecycle_rules**
> InlineResponse20055 s3_list_all_lifecycle_rules(bucket)

List all lifecycle rules of a specific bucket

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
bucket = 'bucket_example' # str | bucket name

try:
    # List all lifecycle rules of a specific bucket
    api_response = api_instance.s3_list_all_lifecycle_rules(bucket)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->s3_list_all_lifecycle_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| bucket name | 

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s3_sts_create**
> InlineResponse20060 s3_sts_create(body)

Create an s3 sts token with an assumend role

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
body = wekarestapi.S3StsBody() # S3StsBody | 

try:
    # Create an s3 sts token with an assumend role
    api_response = api_instance.s3_sts_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->s3_sts_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**S3StsBody**](S3StsBody.md)|  | 

### Return type

[**InlineResponse20060**](InlineResponse20060.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_s3_bucket_policy**
> InlineResponse200 set_s3_bucket_policy(body, bucket)

Set S3 bucket policy

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
body = wekarestapi.BucketPolicyBody() # BucketPolicyBody | 
bucket = 'bucket_example' # str | bucket name

try:
    # Set S3 bucket policy
    api_response = api_instance.set_s3_bucket_policy(body, bucket)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->set_s3_bucket_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BucketPolicyBody**](BucketPolicyBody.md)|  | 
 **bucket** | **str**| bucket name | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_s3_bucket_policy_json**
> InlineResponse200 set_s3_bucket_policy_json(body, bucket)

Set S3 bucket policy json

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
body = wekarestapi.BucketPolicyJsonBody() # BucketPolicyJsonBody | 
bucket = 'bucket_example' # str | bucket name

try:
    # Set S3 bucket policy json
    api_response = api_instance.set_s3_bucket_policy_json(body, bucket)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->set_s3_bucket_policy_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BucketPolicyJsonBody**](BucketPolicyJsonBody.md)|  | 
 **bucket** | **str**| bucket name | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_s3_bucket_quota**
> InlineResponse200 set_s3_bucket_quota(body, bucket)

Set S3 bucket quota

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
body = wekarestapi.BucketQuotaBody() # BucketQuotaBody | 
bucket = 'bucket_example' # str | bucket name

try:
    # Set S3 bucket quota
    api_response = api_instance.set_s3_bucket_quota(body, bucket)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->set_s3_bucket_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BucketQuotaBody**](BucketQuotaBody.md)|  | 
 **bucket** | **str**| bucket name | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_s3_bucket_quota**
> InlineResponse200 unset_s3_bucket_quota(bucket)

Unset S3 bucket quota

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
bucket = 'bucket_example' # str | bucket name

try:
    # Unset S3 bucket quota
    api_response = api_instance.unset_s3_bucket_quota(bucket)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->unset_s3_bucket_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| bucket name | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_s3_cluster**
> InlineResponse400 update_s3_cluster(body)

Update S3 cluster

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.S3Api(wekarestapi.ApiClient(configuration))
body = wekarestapi.S3Body() # S3Body | 

try:
    # Update S3 cluster
    api_response = api_instance.update_s3_cluster(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3Api->update_s3_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**S3Body**](S3Body.md)|  | 

### Return type

[**InlineResponse400**](InlineResponse400.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

