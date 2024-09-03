# swagger_client.UtilityApi

All URIs are relative to *https://www.pietsmiet.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_utility_follows**](UtilityApi.md#delete_utility_follows) | **DELETE** /utility/follows | Delete Utility Follows
[**get_utility_comments**](UtilityApi.md#get_utility_comments) | **GET** /utility/comments | Get Utility Comments
[**get_utility_follows**](UtilityApi.md#get_utility_follows) | **GET** /utility/follows | Get Utility Follows
[**get_utility_player**](UtilityApi.md#get_utility_player) | **GET** /utility/player | Get Utility Player
[**post_utility_autobahn**](UtilityApi.md#post_utility_autobahn) | **POST** /utility/autobahn | Post Utility Autobahn
[**post_utility_comments**](UtilityApi.md#post_utility_comments) | **POST** /utility/comments | Post Utility Comments
[**post_utility_comments_by_id_reports**](UtilityApi.md#post_utility_comments_by_id_reports) | **POST** /utility/comments/{id}/reports | Post Utility Comments By ID Reports
[**post_utility_follows**](UtilityApi.md#post_utility_follows) | **POST** /utility/follows | Post Utility Follows
[**post_utility_highlights**](UtilityApi.md#post_utility_highlights) | **POST** /utility/highlights | Post Utility Highlights

# **delete_utility_follows**
> UtilityFollowsDeleteRequest delete_utility_follows(type=type, id=id, priority=priority)

Delete Utility Follows

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Origin-Integrity
configuration = swagger_client.Configuration()
configuration.api_key['X-Origin-Integrity'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Origin-Integrity'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UtilityApi(swagger_client.ApiClient(configuration))
type = 'videoChannel' # str | type (optional) (default to videoChannel)
id = '12' # str | id (optional) (default to 12)
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Delete Utility Follows
    api_response = api_instance.delete_utility_follows(type=type, id=id, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->delete_utility_follows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | [optional] [default to videoChannel]
 **id** | **str**| id | [optional] [default to 12]
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**UtilityFollowsDeleteRequest**](UtilityFollowsDeleteRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_utility_comments**
> UtilityCommentsGetRequest get_utility_comments(order=order, id=id, type=type, page=page, limit=limit, include=include, order_own=order_own, =, by_user=by_user)

Get Utility Comments

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Origin-Integrity
configuration = swagger_client.Configuration()
configuration.api_key['X-Origin-Integrity'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Origin-Integrity'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UtilityApi(swagger_client.ApiClient(configuration))
order = 'popular' # str | order (optional) (default to popular)
id = '79656' # str | id (optional) (default to 79656)
type = 'video' # str | type (optional) (default to video)
page = '1' # str | page (optional) (default to 1)
limit = '45' # str | limit (optional) (default to 45)
include = 'replies' # str | include[] (optional) (default to replies)
order_own = '1' # str | order_own (optional) (default to 1)
 = '1725328339' # str | _ (optional) (default to 1725328339)
by_user = '0' # str | by_user (optional) (default to 0)

try:
    # Get Utility Comments
    api_response = api_instance.get_utility_comments(order=order, id=id, type=type, page=page, limit=limit, include=include, order_own=order_own, =, by_user=by_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->get_utility_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| order | [optional] [default to popular]
 **id** | **str**| id | [optional] [default to 79656]
 **type** | **str**| type | [optional] [default to video]
 **page** | **str**| page | [optional] [default to 1]
 **limit** | **str**| limit | [optional] [default to 45]
 **include** | **str**| include[] | [optional] [default to replies]
 **order_own** | **str**| order_own | [optional] [default to 1]
 **** | **str**| _ | [optional] [default to 1725328339]
 **by_user** | **str**| by_user | [optional] [default to 0]

### Return type

[**UtilityCommentsGetRequest**](UtilityCommentsGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_utility_follows**
> UtilityFollowsGetRequest get_utility_follows(type=type, id=id)

Get Utility Follows

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Origin-Integrity
configuration = swagger_client.Configuration()
configuration.api_key['X-Origin-Integrity'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Origin-Integrity'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UtilityApi(swagger_client.ApiClient(configuration))
type = 'videoChannel' # str | type (optional) (default to videoChannel)
id = '44' # str | id (optional) (default to 44)

try:
    # Get Utility Follows
    api_response = api_instance.get_utility_follows(type=type, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->get_utility_follows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | [optional] [default to videoChannel]
 **id** | **str**| id | [optional] [default to 44]

### Return type

[**UtilityFollowsGetRequest**](UtilityFollowsGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_utility_player**
> UtilityPlayerGetRequest get_utility_player(video=video, preset=preset, priority=priority)

Get Utility Player

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Origin-Integrity
configuration = swagger_client.Configuration()
configuration.api_key['X-Origin-Integrity'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Origin-Integrity'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UtilityApi(swagger_client.ApiClient(configuration))
video = '79656' # str | video (optional) (default to 79656)
preset = 'quality' # str | preset (optional) (default to quality)
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Get Utility Player
    api_response = api_instance.get_utility_player(video=video, preset=preset, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->get_utility_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video** | **str**| video | [optional] [default to 79656]
 **preset** | **str**| preset | [optional] [default to quality]
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**UtilityPlayerGetRequest**](UtilityPlayerGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_utility_autobahn**
> UtilityAutobahnPostRequest1 post_utility_autobahn(body)

Post Utility Autobahn

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Origin-Integrity
configuration = swagger_client.Configuration()
configuration.api_key['X-Origin-Integrity'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Origin-Integrity'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UtilityApi(swagger_client.ApiClient(configuration))
body = swagger_client.UtilityAutobahnPostRequest() # UtilityAutobahnPostRequest | 

try:
    # Post Utility Autobahn
    api_response = api_instance.post_utility_autobahn(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->post_utility_autobahn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UtilityAutobahnPostRequest**](UtilityAutobahnPostRequest.md)|  | 

### Return type

[**UtilityAutobahnPostRequest1**](UtilityAutobahnPostRequest1.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_utility_comments**
> UtilityCommentsPostRequest1 post_utility_comments(body, priority=priority)

Post Utility Comments

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Origin-Integrity
configuration = swagger_client.Configuration()
configuration.api_key['X-Origin-Integrity'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Origin-Integrity'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UtilityApi(swagger_client.ApiClient(configuration))
body = swagger_client.UtilityCommentsPostRequest() # UtilityCommentsPostRequest | 
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Post Utility Comments
    api_response = api_instance.post_utility_comments(body, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->post_utility_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UtilityCommentsPostRequest**](UtilityCommentsPostRequest.md)|  | 
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**UtilityCommentsPostRequest1**](UtilityCommentsPostRequest1.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_utility_comments_by_id_reports**
> UtilityCommentsIDReportsPostRequest post_utility_comments_by_id_reports(id, priority=priority)

Post Utility Comments By ID Reports

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Origin-Integrity
configuration = swagger_client.Configuration()
configuration.api_key['X-Origin-Integrity'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Origin-Integrity'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UtilityApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Post Utility Comments By ID Reports
    api_response = api_instance.post_utility_comments_by_id_reports(id, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->post_utility_comments_by_id_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**UtilityCommentsIDReportsPostRequest**](UtilityCommentsIDReportsPostRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_utility_follows**
> UtilityFollowsPostRequest1 post_utility_follows(body, priority=priority)

Post Utility Follows

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Origin-Integrity
configuration = swagger_client.Configuration()
configuration.api_key['X-Origin-Integrity'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Origin-Integrity'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UtilityApi(swagger_client.ApiClient(configuration))
body = swagger_client.UtilityFollowsPostRequest() # UtilityFollowsPostRequest | 
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Post Utility Follows
    api_response = api_instance.post_utility_follows(body, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->post_utility_follows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UtilityFollowsPostRequest**](UtilityFollowsPostRequest.md)|  | 
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**UtilityFollowsPostRequest1**](UtilityFollowsPostRequest1.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_utility_highlights**
> UtilityHighlightsPostRequest1 post_utility_highlights(body, priority=priority)

Post Utility Highlights

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Origin-Integrity
configuration = swagger_client.Configuration()
configuration.api_key['X-Origin-Integrity'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Origin-Integrity'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UtilityApi(swagger_client.ApiClient(configuration))
body = swagger_client.UtilityHighlightsPostRequest() # UtilityHighlightsPostRequest | 
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Post Utility Highlights
    api_response = api_instance.post_utility_highlights(body, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->post_utility_highlights: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UtilityHighlightsPostRequest**](UtilityHighlightsPostRequest.md)|  | 
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**UtilityHighlightsPostRequest1**](UtilityHighlightsPostRequest1.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

