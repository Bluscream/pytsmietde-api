# swagger_client.SubscriptionsApi

All URIs are relative to *https://www.pietsmiet.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_subscriptions_discounts**](SubscriptionsApi.md#get_subscriptions_discounts) | **GET** /subscriptions/discounts | Get Subscriptions Discounts
[**get_subscriptions_products**](SubscriptionsApi.md#get_subscriptions_products) | **GET** /subscriptions/products | Get Subscriptions Products

# **get_subscriptions_discounts**
> SubscriptionsDiscountsGetRequest get_subscriptions_discounts()

Get Subscriptions Discounts

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))

try:
    # Get Subscriptions Discounts
    api_response = api_instance.get_subscriptions_discounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscriptions_discounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SubscriptionsDiscountsGetRequest**](SubscriptionsDiscountsGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions_products**
> SubscriptionsProductsGetRequest get_subscriptions_products()

Get Subscriptions Products

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))

try:
    # Get Subscriptions Products
    api_response = api_instance.get_subscriptions_products()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscriptions_products: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SubscriptionsProductsGetRequest**](SubscriptionsProductsGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

