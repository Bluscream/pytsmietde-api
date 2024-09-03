# swagger_client.SchedulesApi

All URIs are relative to *https://www.pietsmiet.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_schedules**](SchedulesApi.md#get_schedules) | **GET** /schedules | Get Schedules
[**get_schedules_upcoming**](SchedulesApi.md#get_schedules_upcoming) | **GET** /schedules/upcoming | Get Schedules Upcoming

# **get_schedules**
> SchedulesGetRequest get_schedules()

Get Schedules

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
api_instance = swagger_client.SchedulesApi(swagger_client.ApiClient(configuration))

try:
    # Get Schedules
    api_response = api_instance.get_schedules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulesApi->get_schedules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SchedulesGetRequest**](SchedulesGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedules_upcoming**
> SchedulesUpcomingGetRequest get_schedules_upcoming()

Get Schedules Upcoming

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
api_instance = swagger_client.SchedulesApi(swagger_client.ApiClient(configuration))

try:
    # Get Schedules Upcoming
    api_response = api_instance.get_schedules_upcoming()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulesApi->get_schedules_upcoming: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SchedulesUpcomingGetRequest**](SchedulesUpcomingGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

