# swagger_client.TagsApi

All URIs are relative to *https://www.pietsmiet.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tags**](TagsApi.md#get_tags) | **GET** /tags | Get Tags

# **get_tags**
> TagsGetRequest get_tags(id=id, type=type)

Get Tags

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
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
id = '79656' # str | id (optional) (default to 79656)
type = 'video' # str | type (optional) (default to video)

try:
    # Get Tags
    api_response = api_instance.get_tags(id=id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | [optional] [default to 79656]
 **type** | **str**| type | [optional] [default to video]

### Return type

[**TagsGetRequest**](TagsGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

