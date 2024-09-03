# swagger_client.PodcastApi

All URIs are relative to *https://www.pietsmiet.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_podcast_categories**](PodcastApi.md#get_podcast_categories) | **GET** /podcast/categories | Get Podcast Categories
[**get_podcast_episodes**](PodcastApi.md#get_podcast_episodes) | **GET** /podcast/episodes | Get Podcast Episodes
[**get_podcast_episodes_by_id**](PodcastApi.md#get_podcast_episodes_by_id) | **GET** /podcast/episodes/{id} | Get Podcast Episodes By ID

# **get_podcast_categories**
> PodcastCategoriesGetRequest get_podcast_categories()

Get Podcast Categories

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
api_instance = swagger_client.PodcastApi(swagger_client.ApiClient(configuration))

try:
    # Get Podcast Categories
    api_response = api_instance.get_podcast_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PodcastApi->get_podcast_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PodcastCategoriesGetRequest**](PodcastCategoriesGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_podcast_episodes**
> PodcastEpisodesGetRequest get_podcast_episodes(page=page, limit=limit)

Get Podcast Episodes

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
api_instance = swagger_client.PodcastApi(swagger_client.ApiClient(configuration))
page = '1' # str | page (optional) (default to 1)
limit = '12' # str | limit (optional) (default to 12)

try:
    # Get Podcast Episodes
    api_response = api_instance.get_podcast_episodes(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PodcastApi->get_podcast_episodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| page | [optional] [default to 1]
 **limit** | **str**| limit | [optional] [default to 12]

### Return type

[**PodcastEpisodesGetRequest**](PodcastEpisodesGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_podcast_episodes_by_id**
> PodcastEpisodesIDGetRequest get_podcast_episodes_by_id(id)

Get Podcast Episodes By ID

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
api_instance = swagger_client.PodcastApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Get Podcast Episodes By ID
    api_response = api_instance.get_podcast_episodes_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PodcastApi->get_podcast_episodes_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PodcastEpisodesIDGetRequest**](PodcastEpisodesIDGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

