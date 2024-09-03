# swagger_client.CommunityApi

All URIs are relative to *https://www.pietsmiet.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_community_suggestions**](CommunityApi.md#get_community_suggestions) | **GET** /community/suggestions | Get Community Suggestions

# **get_community_suggestions**
> CommunitySuggestionsGetRequest get_community_suggestions(page=page, limit=limit, order=order, statuses=statuses)

Get Community Suggestions

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
api_instance = swagger_client.CommunityApi(swagger_client.ApiClient(configuration))
page = '1' # str | page (optional) (default to 1)
limit = '2' # str | limit (optional) (default to 2)
order = 'latest' # str | order (optional) (default to latest)
statuses = 'open' # str | statuses[] (optional) (default to open)

try:
    # Get Community Suggestions
    api_response = api_instance.get_community_suggestions(page=page, limit=limit, order=order, statuses=statuses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunityApi->get_community_suggestions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| page | [optional] [default to 1]
 **limit** | **str**| limit | [optional] [default to 2]
 **order** | **str**| order | [optional] [default to latest]
 **statuses** | **str**| statuses[] | [optional] [default to open]

### Return type

[**CommunitySuggestionsGetRequest**](CommunitySuggestionsGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

