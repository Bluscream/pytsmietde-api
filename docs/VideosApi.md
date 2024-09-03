# swagger_client.VideosApi

All URIs are relative to *https://www.pietsmiet.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_channel_video_count**](VideosApi.md#get_channel_video_count) | **GET** /videos/channels/{id} | Get Channel Video Count
[**get_videos**](VideosApi.md#get_videos) | **GET** /videos | Get Videos
[**get_videos_authors**](VideosApi.md#get_videos_authors) | **GET** /videos/authors | Get Videos Authors
[**get_videos_by_id**](VideosApi.md#get_videos_by_id) | **GET** /videos/{id} | Get Videos By ID
[**get_videos_by_id_next**](VideosApi.md#get_videos_by_id_next) | **GET** /videos/{id}/next | Get Videos By ID Next
[**get_videos_channels**](VideosApi.md#get_videos_channels) | **GET** /videos/channels | Get Videos Channels
[**get_videos_clips**](VideosApi.md#get_videos_clips) | **GET** /videos/clips | Get Videos Clips
[**get_videos_playlists**](VideosApi.md#get_videos_playlists) | **GET** /videos/playlists | Get Videos Playlists
[**get_videos_playlists_by_id**](VideosApi.md#get_videos_playlists_by_id) | **GET** /videos/playlists/{id} | Get Videos Playlists By ID
[**post_videos_clips**](VideosApi.md#post_videos_clips) | **POST** /videos/clips | Post Videos Clips
[**post_videos_playlists_by_id**](VideosApi.md#post_videos_playlists_by_id) | **POST** /videos/playlists/{id}/videos | Post Videos Playlists By ID

# **get_channel_video_count**
> ChannelVideoCountGetRequest get_channel_video_count(id)

Get Channel Video Count

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
api_instance = swagger_client.VideosApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Get Channel Video Count
    api_response = api_instance.get_channel_video_count(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_channel_video_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ChannelVideoCountGetRequest**](ChannelVideoCountGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos**
> VideosGetRequest get_videos(limit=limit, order=order, prioritize_featured=prioritize_featured, page=page, liked_by=liked_by, viewed_by=viewed_by, priority=priority, followed_by=followed_by, playlists=playlists, =, channels=channels, playlist_video=playlist_video)

Get Videos

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
api_instance = swagger_client.VideosApi(swagger_client.ApiClient(configuration))
limit = '15' # str | limit (optional) (default to 15)
order = 'latest' # str | order (optional) (default to latest)
prioritize_featured = '1' # str | prioritize_featured (optional) (default to 1)
page = '1' # str | page (optional) (default to 1)
liked_by = '0' # str | liked_by (optional) (default to 0)
viewed_by = '0' # str | viewed_by (optional) (default to 0)
priority = 'u=0' # str | Priority (optional) (default to u=0)
followed_by = '0' # str | followed_by (optional) (default to 0)
playlists = '15196' # str | playlists[] (optional) (default to 15196)
 = '1725328864' # str | _ (optional) (default to 1725328864)
channels = '44' # str | channels[] (optional) (default to 44)
playlist_video = '79576' # str | playlist_video (optional) (default to 79576)

try:
    # Get Videos
    api_response = api_instance.get_videos(limit=limit, order=order, prioritize_featured=prioritize_featured, page=page, liked_by=liked_by, viewed_by=viewed_by, priority=priority, followed_by=followed_by, playlists=playlists, =, channels=channels, playlist_video=playlist_video)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | [optional] [default to 15]
 **order** | **str**| order | [optional] [default to latest]
 **prioritize_featured** | **str**| prioritize_featured | [optional] [default to 1]
 **page** | **str**| page | [optional] [default to 1]
 **liked_by** | **str**| liked_by | [optional] [default to 0]
 **viewed_by** | **str**| viewed_by | [optional] [default to 0]
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]
 **followed_by** | **str**| followed_by | [optional] [default to 0]
 **playlists** | **str**| playlists[] | [optional] [default to 15196]
 **** | **str**| _ | [optional] [default to 1725328864]
 **channels** | **str**| channels[] | [optional] [default to 44]
 **playlist_video** | **str**| playlist_video | [optional] [default to 79576]

### Return type

[**VideosGetRequest**](VideosGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_authors**
> VideosAuthorsGetRequest get_videos_authors()

Get Videos Authors

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
api_instance = swagger_client.VideosApi(swagger_client.ApiClient(configuration))

try:
    # Get Videos Authors
    api_response = api_instance.get_videos_authors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_videos_authors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VideosAuthorsGetRequest**](VideosAuthorsGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_by_id**
> VideosIDGetRequest get_videos_by_id(id, include=include)

Get Videos By ID

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
api_instance = swagger_client.VideosApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
include = 'playlist' # str | include[] (optional) (default to playlist)

try:
    # Get Videos By ID
    api_response = api_instance.get_videos_by_id(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_videos_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **include** | **str**| include[] | [optional] [default to playlist]

### Return type

[**VideosIDGetRequest**](VideosIDGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_by_id_next**
> VideosIDNextGetRequest get_videos_by_id_next(id, playlist=playlist, channel=channel)

Get Videos By ID Next

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
api_instance = swagger_client.VideosApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
playlist = '155942' # str | playlist (optional) (default to 155942)
channel = '12' # str | channel (optional) (default to 12)

try:
    # Get Videos By ID Next
    api_response = api_instance.get_videos_by_id_next(id, playlist=playlist, channel=channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_videos_by_id_next: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **playlist** | **str**| playlist | [optional] [default to 155942]
 **channel** | **str**| channel | [optional] [default to 12]

### Return type

[**VideosIDNextGetRequest**](VideosIDNextGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_channels**
> VideosChannelsGetRequest get_videos_channels(page=page, order=order)

Get Videos Channels

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
api_instance = swagger_client.VideosApi(swagger_client.ApiClient(configuration))
page = '1' # str | page (optional) (default to 1)
order = 'videos' # str | order (optional) (default to videos)

try:
    # Get Videos Channels
    api_response = api_instance.get_videos_channels(page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_videos_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| page | [optional] [default to 1]
 **order** | **str**| order | [optional] [default to videos]

### Return type

[**VideosChannelsGetRequest**](VideosChannelsGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_clips**
> VideosClipsGetRequest get_videos_clips(video=video, limit=limit, order=order, page=page)

Get Videos Clips

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
api_instance = swagger_client.VideosApi(swagger_client.ApiClient(configuration))
video = '79656' # str | video (optional) (default to 79656)
limit = '4' # str | limit (optional) (default to 4)
order = 'popular' # str | order (optional) (default to popular)
page = '1' # str | page (optional) (default to 1)

try:
    # Get Videos Clips
    api_response = api_instance.get_videos_clips(video=video, limit=limit, order=order, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_videos_clips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video** | **str**| video | [optional] [default to 79656]
 **limit** | **str**| limit | [optional] [default to 4]
 **order** | **str**| order | [optional] [default to popular]
 **page** | **str**| page | [optional] [default to 1]

### Return type

[**VideosClipsGetRequest**](VideosClipsGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_playlists**
> VideosPlaylistsGetRequest get_videos_playlists(user=user, page=page, order=order, limit=limit)

Get Videos Playlists

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
api_instance = swagger_client.VideosApi(swagger_client.ApiClient(configuration))
user = '0' # str | user (optional) (default to 0)
page = '1' # str | page (optional) (default to 1)
order = 'latest' # str | order (optional) (default to latest)
limit = '18' # str | limit (optional) (default to 18)

try:
    # Get Videos Playlists
    api_response = api_instance.get_videos_playlists(user=user, page=page, order=order, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_videos_playlists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| user | [optional] [default to 0]
 **page** | **str**| page | [optional] [default to 1]
 **order** | **str**| order | [optional] [default to latest]
 **limit** | **str**| limit | [optional] [default to 18]

### Return type

[**VideosPlaylistsGetRequest**](VideosPlaylistsGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_playlists_by_id**
> VideosPlaylistsIDGetRequest get_videos_playlists_by_id(id)

Get Videos Playlists By ID

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
api_instance = swagger_client.VideosApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Get Videos Playlists By ID
    api_response = api_instance.get_videos_playlists_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_videos_playlists_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**VideosPlaylistsIDGetRequest**](VideosPlaylistsIDGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_videos_clips**
> VideosClipsPostRequest1 post_videos_clips(body, priority=priority)

Post Videos Clips

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
api_instance = swagger_client.VideosApi(swagger_client.ApiClient(configuration))
body = swagger_client.VideosClipsPostRequest() # VideosClipsPostRequest | 
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Post Videos Clips
    api_response = api_instance.post_videos_clips(body, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->post_videos_clips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VideosClipsPostRequest**](VideosClipsPostRequest.md)|  | 
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**VideosClipsPostRequest1**](VideosClipsPostRequest1.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_videos_playlists_by_id**
> VideosPlaylistsIDPostRequest1 post_videos_playlists_by_id(body, id, priority=priority)

Post Videos Playlists By ID

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
api_instance = swagger_client.VideosApi(swagger_client.ApiClient(configuration))
body = swagger_client.VideosPlaylistsIDPostRequest() # VideosPlaylistsIDPostRequest | 
id = 56 # int | 
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Post Videos Playlists By ID
    api_response = api_instance.post_videos_playlists_by_id(body, id, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->post_videos_playlists_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VideosPlaylistsIDPostRequest**](VideosPlaylistsIDPostRequest.md)|  | 
 **id** | **int**|  | 
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**VideosPlaylistsIDPostRequest1**](VideosPlaylistsIDPostRequest1.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

