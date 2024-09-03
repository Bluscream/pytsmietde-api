# swagger_client.SearchApi

All URIs are relative to *https://www.pietsmiet.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_search**](SearchApi.md#get_search) | **GET** /search | Get Search

# **get_search**
> SearchGetRequest get_search(query=query, part=part, page=page, priority=priority)

Get Search

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
query = 'test' # str | query (optional) (default to test)
part = 'videos' # str | part (optional) (default to videos)
page = '1' # str | page (optional) (default to 1)
priority = 'u=0' # str | Priority (optional) (default to u=0)

try:
    # Get Search
    api_response = api_instance.get_search(query=query, part=part, page=page, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| query | [optional] [default to test]
 **part** | **str**| part | [optional] [default to videos]
 **page** | **str**| page | [optional] [default to 1]
 **priority** | **str**| Priority | [optional] [default to u&#x3D;0]

### Return type

[**SearchGetRequest**](SearchGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

