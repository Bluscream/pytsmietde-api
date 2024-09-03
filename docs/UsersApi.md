# swagger_client.UsersApi

All URIs are relative to *https://www.pietsmiet.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_users_by_id_tokens_id**](UsersApi.md#delete_users_by_id_tokens_id) | **DELETE** /users/{id}/tokens/{token} | Delete Tokens by User Id
[**delete_users_object20_object_tokens**](UsersApi.md#delete_users_object20_object_tokens) | **DELETE** /users/{id}/tokens | Delete Users Object 20 Object Tokens
[**get_users_by_id**](UsersApi.md#get_users_by_id) | **GET** /users/{id} | Get Users By ID
[**get_users_by_id_achievements**](UsersApi.md#get_users_by_id_achievements) | **GET** /users/{id}/achievements | Get Users By ID Achievements
[**get_users_by_id_dislikes**](UsersApi.md#get_users_by_id_dislikes) | **GET** /users/{id}/dislikes | Get Users By ID Dislikes
[**get_users_by_id_followings**](UsersApi.md#get_users_by_id_followings) | **GET** /users/{id}/followings | Get Users By ID Followings
[**get_users_by_id_invoices**](UsersApi.md#get_users_by_id_invoices) | **GET** /users/{id}/invoices | Get Users By ID Invoices
[**get_users_by_id_likes**](UsersApi.md#get_users_by_id_likes) | **GET** /users/{id}/likes | Get Users By ID Likes
[**get_users_by_id_notifications**](UsersApi.md#get_users_by_id_notifications) | **GET** /users/{id}/notifications | Get Users By ID Notifications
[**get_users_by_id_settings_notifications**](UsersApi.md#get_users_by_id_settings_notifications) | **GET** /users/{id}/settings/notifications | Get Users By ID Settings Notifications
[**get_users_by_id_settings_twofactor_setup**](UsersApi.md#get_users_by_id_settings_twofactor_setup) | **GET** /users/{id}/settings/twofactor/setup | Get Users By ID Settings Twofactor Setup
[**get_users_by_id_subscriptions**](UsersApi.md#get_users_by_id_subscriptions) | **GET** /users/{id}/subscriptions | Get Users By ID Subscriptions
[**get_users_by_id_tokens**](UsersApi.md#get_users_by_id_tokens) | **GET** /users/{id}/tokens | Get Users By ID Tokens
[**get_users_by_id_views**](UsersApi.md#get_users_by_id_views) | **GET** /users/{id}/views | Get Users By ID Views
[**get_users_me**](UsersApi.md#get_users_me) | **GET** /users/@me | Get Users Me
[**patch_users_by_id_notifications_by_uuid**](UsersApi.md#patch_users_by_id_notifications_by_uuid) | **PATCH** /users/{id}/notifications/{uuid} | Patch Users By ID Notifications By UUID
[**patch_users_by_id_settings_notifications**](UsersApi.md#patch_users_by_id_settings_notifications) | **PATCH** /users/{id}/settings/notifications | Patch Users By ID Settings Notifications
[**patch_users_by_id_settings_password**](UsersApi.md#patch_users_by_id_settings_password) | **PATCH** /users/{id}/settings/password | Patch Users By ID Settings Password
[**patch_users_by_id_settings_preferences**](UsersApi.md#patch_users_by_id_settings_preferences) | **PATCH** /users/{id}/settings/preferences | Patch Users By ID Settings Preferences
[**patch_users_by_id_settings_profile**](UsersApi.md#patch_users_by_id_settings_profile) | **PATCH** /users/{id}/settings/profile | Patch Users By ID Settings Profile
[**post_users_by_id_dislikes**](UsersApi.md#post_users_by_id_dislikes) | **POST** /users/{id}/dislikes | Post Users By ID Dislikes
[**post_users_by_id_likes**](UsersApi.md#post_users_by_id_likes) | **POST** /users/{id}/likes | Post Users By ID Likes
[**post_users_by_id_settings_assets**](UsersApi.md#post_users_by_id_settings_assets) | **POST** /users/{id}/settings/assets | Post Users By ID Settings Assets
[**post_users_by_id_settings_data_request**](UsersApi.md#post_users_by_id_settings_data_request) | **POST** /users/{id}/settings/data/request | Post Users By ID Settings Data Request
[**post_users_by_id_settings_twofactor_reset**](UsersApi.md#post_users_by_id_settings_twofactor_reset) | **POST** /users/{id}/settings/twofactor/reset | Post Users By ID Settings Twofactor Reset
[**post_users_by_id_settings_twofactor_setup**](UsersApi.md#post_users_by_id_settings_twofactor_setup) | **POST** /users/{id}/settings/twofactor/setup | Post Users By ID Settings Twofactor Setup

# **delete_users_by_id_tokens_id**
> UsersIDTokensTokenDeleteRequest delete_users_by_id_tokens_id(id, token, priority=priority)

Delete Tokens by User Id

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
token = 56 # int | 
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Delete Tokens by User Id
    api_response = api_instance.delete_users_by_id_tokens_id(id, token, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_users_by_id_tokens_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **token** | **int**|  | 
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**UsersIDTokensTokenDeleteRequest**](UsersIDTokensTokenDeleteRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_users_object20_object_tokens**
> delete_users_object20_object_tokens(id, priority=priority)

Delete Users Object 20 Object Tokens

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Delete Users Object 20 Object Tokens
    api_instance.delete_users_object20_object_tokens(id, priority=priority)
except ApiException as e:
    print("Exception when calling UsersApi->delete_users_object20_object_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

void (empty response body)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_id**
> UsersIDGetRequest get_users_by_id(id)

Get Users By ID

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Get Users By ID
    api_response = api_instance.get_users_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UsersIDGetRequest**](UsersIDGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_id_achievements**
> UsersIDAchievementsGetRequest get_users_by_id_achievements(id)

Get Users By ID Achievements

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Get Users By ID Achievements
    api_response = api_instance.get_users_by_id_achievements(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_by_id_achievements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UsersIDAchievementsGetRequest**](UsersIDAchievementsGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_id_dislikes**
> UsersIDDislikesGetRequest get_users_by_id_dislikes(id)

Get Users By ID Dislikes

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Get Users By ID Dislikes
    api_response = api_instance.get_users_by_id_dislikes(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_by_id_dislikes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UsersIDDislikesGetRequest**](UsersIDDislikesGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_id_followings**
> UsersIDFollowingsGetRequest get_users_by_id_followings(id)

Get Users By ID Followings

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Get Users By ID Followings
    api_response = api_instance.get_users_by_id_followings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_by_id_followings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UsersIDFollowingsGetRequest**](UsersIDFollowingsGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_id_invoices**
> UsersIDInvoicesGetRequest get_users_by_id_invoices(id)

Get Users By ID Invoices

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Get Users By ID Invoices
    api_response = api_instance.get_users_by_id_invoices(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_by_id_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UsersIDInvoicesGetRequest**](UsersIDInvoicesGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_id_likes**
> UsersIDLikesGetRequest get_users_by_id_likes(id)

Get Users By ID Likes

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Get Users By ID Likes
    api_response = api_instance.get_users_by_id_likes(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_by_id_likes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UsersIDLikesGetRequest**](UsersIDLikesGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_id_notifications**
> UsersIDNotificationsGetRequest get_users_by_id_notifications(id)

Get Users By ID Notifications

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Get Users By ID Notifications
    api_response = api_instance.get_users_by_id_notifications(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_by_id_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UsersIDNotificationsGetRequest**](UsersIDNotificationsGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_id_settings_notifications**
> UsersIDSettingsNotificationsGetRequest get_users_by_id_settings_notifications(id)

Get Users By ID Settings Notifications

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Get Users By ID Settings Notifications
    api_response = api_instance.get_users_by_id_settings_notifications(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_by_id_settings_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UsersIDSettingsNotificationsGetRequest**](UsersIDSettingsNotificationsGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_id_settings_twofactor_setup**
> UsersIDSettingsTwofactorSetupGetRequest get_users_by_id_settings_twofactor_setup(id, priority=priority)

Get Users By ID Settings Twofactor Setup

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Get Users By ID Settings Twofactor Setup
    api_response = api_instance.get_users_by_id_settings_twofactor_setup(id, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_by_id_settings_twofactor_setup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**UsersIDSettingsTwofactorSetupGetRequest**](UsersIDSettingsTwofactorSetupGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_id_subscriptions**
> UsersIDSubscriptionsGetRequest get_users_by_id_subscriptions(id, include=include)

Get Users By ID Subscriptions

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
include = 'braintree' # str | include[] (optional) (default to braintree)

try:
    # Get Users By ID Subscriptions
    api_response = api_instance.get_users_by_id_subscriptions(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_by_id_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **include** | **str**| include[] | [optional] [default to braintree]

### Return type

[**UsersIDSubscriptionsGetRequest**](UsersIDSubscriptionsGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_id_tokens**
> UsersIDTokensGetRequest get_users_by_id_tokens(id)

Get Users By ID Tokens

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Get Users By ID Tokens
    api_response = api_instance.get_users_by_id_tokens(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_by_id_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UsersIDTokensGetRequest**](UsersIDTokensGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_id_views**
> UsersIDViewsGetRequest get_users_by_id_views(id)

Get Users By ID Views

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Get Users By ID Views
    api_response = api_instance.get_users_by_id_views(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_by_id_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UsersIDViewsGetRequest**](UsersIDViewsGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_me**
> UsersMeGetRequest get_users_me()

Get Users Me

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # Get Users Me
    api_response = api_instance.get_users_me()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_me: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UsersMeGetRequest**](UsersMeGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_users_by_id_notifications_by_uuid**
> UsersIDNotificationsUUIDPatchRequest1 patch_users_by_id_notifications_by_uuid(body, id, uuid, priority=priority)

Patch Users By ID Notifications By UUID

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersIDNotificationsUUIDPatchRequest() # UsersIDNotificationsUUIDPatchRequest | 
id = 56 # int | 
uuid = 'uuid_example' # str | 
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Patch Users By ID Notifications By UUID
    api_response = api_instance.patch_users_by_id_notifications_by_uuid(body, id, uuid, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_users_by_id_notifications_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersIDNotificationsUUIDPatchRequest**](UsersIDNotificationsUUIDPatchRequest.md)|  | 
 **id** | **int**|  | 
 **uuid** | **str**|  | 
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**UsersIDNotificationsUUIDPatchRequest1**](UsersIDNotificationsUUIDPatchRequest1.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_users_by_id_settings_notifications**
> UsersIDSettingsNotificationsPatchRequest1 patch_users_by_id_settings_notifications(body, id, priority=priority)

Patch Users By ID Settings Notifications

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersIDSettingsNotificationsPatchRequest() # UsersIDSettingsNotificationsPatchRequest | 
id = 56 # int | 
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Patch Users By ID Settings Notifications
    api_response = api_instance.patch_users_by_id_settings_notifications(body, id, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_users_by_id_settings_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersIDSettingsNotificationsPatchRequest**](UsersIDSettingsNotificationsPatchRequest.md)|  | 
 **id** | **int**|  | 
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**UsersIDSettingsNotificationsPatchRequest1**](UsersIDSettingsNotificationsPatchRequest1.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_users_by_id_settings_password**
> UsersIDSettingsPasswordPatchRequest1 patch_users_by_id_settings_password(body, id, priority=priority)

Patch Users By ID Settings Password

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersIDSettingsPasswordPatchRequest() # UsersIDSettingsPasswordPatchRequest | 
id = 56 # int | 
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Patch Users By ID Settings Password
    api_response = api_instance.patch_users_by_id_settings_password(body, id, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_users_by_id_settings_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersIDSettingsPasswordPatchRequest**](UsersIDSettingsPasswordPatchRequest.md)|  | 
 **id** | **int**|  | 
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**UsersIDSettingsPasswordPatchRequest1**](UsersIDSettingsPasswordPatchRequest1.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_users_by_id_settings_preferences**
> UsersIDSettingsPreferencesPatchRequest1 patch_users_by_id_settings_preferences(body, id, priority=priority)

Patch Users By ID Settings Preferences

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersIDSettingsPreferencesPatchRequest() # UsersIDSettingsPreferencesPatchRequest | 
id = 56 # int | 
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Patch Users By ID Settings Preferences
    api_response = api_instance.patch_users_by_id_settings_preferences(body, id, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_users_by_id_settings_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersIDSettingsPreferencesPatchRequest**](UsersIDSettingsPreferencesPatchRequest.md)|  | 
 **id** | **int**|  | 
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**UsersIDSettingsPreferencesPatchRequest1**](UsersIDSettingsPreferencesPatchRequest1.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_users_by_id_settings_profile**
> UsersIDSettingsProfilePatchRequest1 patch_users_by_id_settings_profile(body, id, priority=priority)

Patch Users By ID Settings Profile

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersIDSettingsProfilePatchRequest() # UsersIDSettingsProfilePatchRequest | 
id = 56 # int | 
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Patch Users By ID Settings Profile
    api_response = api_instance.patch_users_by_id_settings_profile(body, id, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_users_by_id_settings_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersIDSettingsProfilePatchRequest**](UsersIDSettingsProfilePatchRequest.md)|  | 
 **id** | **int**|  | 
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**UsersIDSettingsProfilePatchRequest1**](UsersIDSettingsProfilePatchRequest1.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_id_dislikes**
> UsersIDDislikesPostRequest1 post_users_by_id_dislikes(body, id, priority=priority)

Post Users By ID Dislikes

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersIDDislikesPostRequest() # UsersIDDislikesPostRequest | 
id = 56 # int | 
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Post Users By ID Dislikes
    api_response = api_instance.post_users_by_id_dislikes(body, id, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_users_by_id_dislikes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersIDDislikesPostRequest**](UsersIDDislikesPostRequest.md)|  | 
 **id** | **int**|  | 
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**UsersIDDislikesPostRequest1**](UsersIDDislikesPostRequest1.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_id_likes**
> UsersIDLikesPostRequest1 post_users_by_id_likes(body, id, priority=priority)

Post Users By ID Likes

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersIDLikesPostRequest() # UsersIDLikesPostRequest | 
id = 56 # int | 
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Post Users By ID Likes
    api_response = api_instance.post_users_by_id_likes(body, id, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_users_by_id_likes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersIDLikesPostRequest**](UsersIDLikesPostRequest.md)|  | 
 **id** | **int**|  | 
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**UsersIDLikesPostRequest1**](UsersIDLikesPostRequest1.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_id_settings_assets**
> UsersIDSettingsAssetsPostRequest post_users_by_id_settings_assets(id, priority=priority)

Post Users By ID Settings Assets

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Post Users By ID Settings Assets
    api_response = api_instance.post_users_by_id_settings_assets(id, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_users_by_id_settings_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**UsersIDSettingsAssetsPostRequest**](UsersIDSettingsAssetsPostRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_id_settings_data_request**
> UsersIDSettingsDataRequestPostRequest post_users_by_id_settings_data_request(id, priority=priority)

Post Users By ID Settings Data Request

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Post Users By ID Settings Data Request
    api_response = api_instance.post_users_by_id_settings_data_request(id, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_users_by_id_settings_data_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**UsersIDSettingsDataRequestPostRequest**](UsersIDSettingsDataRequestPostRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_id_settings_twofactor_reset**
> UsersIDSettingsTwofactorResetPostRequest1 post_users_by_id_settings_twofactor_reset(body, id, priority=priority)

Post Users By ID Settings Twofactor Reset

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersIDSettingsTwofactorResetPostRequest() # UsersIDSettingsTwofactorResetPostRequest | 
id = 56 # int | 
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Post Users By ID Settings Twofactor Reset
    api_response = api_instance.post_users_by_id_settings_twofactor_reset(body, id, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_users_by_id_settings_twofactor_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersIDSettingsTwofactorResetPostRequest**](UsersIDSettingsTwofactorResetPostRequest.md)|  | 
 **id** | **int**|  | 
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**UsersIDSettingsTwofactorResetPostRequest1**](UsersIDSettingsTwofactorResetPostRequest1.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_id_settings_twofactor_setup**
> UsersIDSettingsTwofactorSetupPostRequest1 post_users_by_id_settings_twofactor_setup(body, id, priority=priority)

Post Users By ID Settings Twofactor Setup

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersIDSettingsTwofactorSetupPostRequest() # UsersIDSettingsTwofactorSetupPostRequest | 
id = 56 # int | 
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Post Users By ID Settings Twofactor Setup
    api_response = api_instance.post_users_by_id_settings_twofactor_setup(body, id, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_users_by_id_settings_twofactor_setup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersIDSettingsTwofactorSetupPostRequest**](UsersIDSettingsTwofactorSetupPostRequest.md)|  | 
 **id** | **int**|  | 
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**UsersIDSettingsTwofactorSetupPostRequest1**](UsersIDSettingsTwofactorSetupPostRequest1.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

