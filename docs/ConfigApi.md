# swagger_client.ConfigApi

All URIs are relative to *https://www.pietsmiet.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config_asset_version**](ConfigApi.md#get_config_asset_version) | **GET** /config/asset_version | Get Config Asset Version
[**get_config_enumerations_countries**](ConfigApi.md#get_config_enumerations_countries) | **GET** /config/enumerations/countries | Get Config Enumerations Countries
[**get_x_origin_integrity_header**](ConfigApi.md#get_x_origin_integrity_header) | **GET** /config/i | Get X-Origin-Integrity Header

# **get_config_asset_version**
> ConfigAssetVersionGetRequest get_config_asset_version()

Get Config Asset Version

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
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))

try:
    # Get Config Asset Version
    api_response = api_instance.get_config_asset_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_config_asset_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigAssetVersionGetRequest**](ConfigAssetVersionGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_enumerations_countries**
> ConfigEnumerationsCountriesGetRequest get_config_enumerations_countries()

Get Config Enumerations Countries

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
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))

try:
    # Get Config Enumerations Countries
    api_response = api_instance.get_config_enumerations_countries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_config_enumerations_countries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigEnumerationsCountriesGetRequest**](ConfigEnumerationsCountriesGetRequest.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_x_origin_integrity_header**
> ConfigOriginIntegrityHeader get_x_origin_integrity_header()

Get X-Origin-Integrity Header

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
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))

try:
    # Get X-Origin-Integrity Header
    api_response = api_instance.get_x_origin_integrity_header()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_x_origin_integrity_header: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigOriginIntegrityHeader**](ConfigOriginIntegrityHeader.md)

### Authorization

[X-Origin-Integrity](../README.md#X-Origin-Integrity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

