# coding: utf-8

"""
    Pietsmiet.de API

    OpenAPI spec generated from HAR data for www.pietsmiet.de on 2024-09-03T03:22:16.459Z  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient
import sys
maxint = sys.maxsize * 2 + 1


class PodcastApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_podcast_categories(self, **kwargs):  # noqa: E501
        """Get Podcast Categories  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_podcast_categories(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PodcastCategoriesGetRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_podcast_categories_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_podcast_categories_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_podcast_categories_with_http_info(self, **kwargs):  # noqa: E501
        """Get Podcast Categories  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_podcast_categories_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PodcastCategoriesGetRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_podcast_categories" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Origin-Integrity']  # noqa: E501

        return self.api_client.call_api(
            '/podcast/categories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PodcastCategoriesGetRequest',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_podcast_episodes(self, **kwargs):  # noqa: E501 # page=None, limit=None, 
        """Get Podcast Episodes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_podcast_episodes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page: page # Default: 1
        :param str limit: limit # Max: 100
        :return: PodcastEpisodesGetRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        _page = kwargs.get('page', None)
        if _page and (_page > maxint or _page < 1): raise Exception(f"?page={_page} must be between 1 and {maxint}!")
        _limit = kwargs.get('limit', None)
        if _limit and (_limit > 100 or _limit < 1): raise Exception(f"?limit={_limit} must be between 1 and 100!")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_podcast_episodes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_podcast_episodes_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_podcast_episodes_with_http_info(self, **kwargs):  # noqa: E501
        """Get Podcast Episodes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_podcast_episodes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page: page
        :param str limit: limit
        :return: PodcastEpisodesGetRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_podcast_episodes" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Origin-Integrity']  # noqa: E501

        return self.api_client.call_api(
            '/podcast/episodes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PodcastEpisodesGetRequest',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_podcast_episodes_by_id(self, id, **kwargs):  # noqa: E501
        """Get Podcast Episodes By ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_podcast_episodes_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: PodcastEpisodesIDGetRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_podcast_episodes_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_podcast_episodes_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_podcast_episodes_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Podcast Episodes By ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_podcast_episodes_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: PodcastEpisodesIDGetRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_podcast_episodes_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_podcast_episodes_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Origin-Integrity']  # noqa: E501

        return self.api_client.call_api(
            '/podcast/episodes/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PodcastEpisodesIDGetRequest',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
