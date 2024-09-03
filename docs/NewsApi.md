# swagger_client.NewsApi

All URIs are relative to *https://www.pietsmiet.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_news_articles**](NewsApi.md#get_news_articles) | **GET** /news/articles | Get News Articles
[**get_news_articles_by_id**](NewsApi.md#get_news_articles_by_id) | **GET** /news/articles/{id} | Get News Articles By ID
[**get_news_categories_id**](NewsApi.md#get_news_categories_id) | **GET** /news/categories/{id} | Get News Categories 34

# **get_news_articles**
> NewsArticlesGetRequest get_news_articles(limit=limit, order=order, categories=categories, page=page, category=category)

Get News Articles

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
api_instance = swagger_client.NewsApi(swagger_client.ApiClient(configuration))
limit = '2' # str | limit (optional) (default to 2)
order = 'featured' # str | order (optional) (default to featured)
categories = '34' # str | categories[] (optional) (default to 34)
page = '1' # str | page (optional) (default to 1)
category = '34' # str | category (optional) (default to 34)

try:
    # Get News Articles
    api_response = api_instance.get_news_articles(limit=limit, order=order, categories=categories, page=page, category=category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->get_news_articles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | [optional] [default to 2]
 **order** | **str**| order | [optional] [default to featured]
 **categories** | **str**| categories[] | [optional] [default to 34]
 **page** | **str**| page | [optional] [default to 1]
 **category** | **str**| category | [optional] [default to 34]

### Return type

[**NewsArticlesGetRequest**](NewsArticlesGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_news_articles_by_id**
> NewsArticlesIDGetRequest get_news_articles_by_id(id)

Get News Articles By ID

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
api_instance = swagger_client.NewsApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Get News Articles By ID
    api_response = api_instance.get_news_articles_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->get_news_articles_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**NewsArticlesIDGetRequest**](NewsArticlesIDGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_news_categories_id**
> NewsCategories34GetRequest get_news_categories_id(id)

Get News Categories 34

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
api_instance = swagger_client.NewsApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Get News Categories 34
    api_response = api_instance.get_news_categories_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->get_news_categories_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**NewsCategories34GetRequest**](NewsCategories34GetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

