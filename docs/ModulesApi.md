# swagger_client.ModulesApi

All URIs are relative to *https://www.pietsmiet.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_modules**](ModulesApi.md#get_modules) | **GET** /modules | Get Modules

# **get_modules**
> ModulesGetRequest get_modules()

Get Modules

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
api_instance = swagger_client.ModulesApi(swagger_client.ApiClient(configuration))

try:
    # Get Modules
    api_response = api_instance.get_modules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModulesApi->get_modules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ModulesGetRequest**](ModulesGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

