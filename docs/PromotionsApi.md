# swagger_client.PromotionsApi

All URIs are relative to *https://www.pietsmiet.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_promotions**](PromotionsApi.md#get_promotions) | **GET** /promotions | Get Promotions

# **get_promotions**
> PromotionsGetRequest get_promotions(ab=ab)

Get Promotions

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
api_instance = swagger_client.PromotionsApi(swagger_client.ApiClient(configuration))
ab = '1' # str | ab (optional) (default to 1)

try:
    # Get Promotions
    api_response = api_instance.get_promotions(ab=ab)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromotionsApi->get_promotions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ab** | **str**| ab | [optional] [default to 1]

### Return type

[**PromotionsGetRequest**](PromotionsGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

