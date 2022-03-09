# coding: utf-8

"""
    @weka-api

    <div>The Weka system supports a RESTful API. This is useful when automating the interaction with the Weka system and when integrating it into your workflows or monitoring systems. The API is accessible at port 14000, via the /api/v2 URL, you can explore it via /api/v2/docs when accessing from the cluster (e.g. https://weka01:14000/api/v2/docs).<div style=\"margin-top: 15px;\">Note: Weka uses 64bit numbers. Please take special care when interacting with the API with different program languages (In JS for example you can use \"json-bigint\")</div></div>  # noqa: E501

    OpenAPI spec version: 3.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class StatsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_real_time_stats(self, **kwargs):  # noqa: E501
        """Get real time stats  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_real_time_stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20077
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_real_time_stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_real_time_stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_real_time_stats_with_http_info(self, **kwargs):  # noqa: E501
        """Get real time stats  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_real_time_stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20077
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
                    " to method get_real_time_stats" % key
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
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stats/realtime', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20077',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stats(self, **kwargs):  # noqa: E501
        """Get stats  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_time:
        :param str end_time:
        :param str interval:
        :param list[str] category: array of categories
        :param list[str] stat:
        :param float resolution_secs:
        :param bool accumulated:
        :param bool per_node:
        :param list[str] node_uids:
        :param list[str] param_param_key:
        :param bool no_zeroes:
        :param bool show_internal:
        :return: InlineResponse20075
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_stats_with_http_info(self, **kwargs):  # noqa: E501
        """Get stats  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_time:
        :param str end_time:
        :param str interval:
        :param list[str] category: array of categories
        :param list[str] stat:
        :param float resolution_secs:
        :param bool accumulated:
        :param bool per_node:
        :param list[str] node_uids:
        :param list[str] param_param_key:
        :param bool no_zeroes:
        :param bool show_internal:
        :return: InlineResponse20075
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_time', 'end_time', 'interval', 'category', 'stat', 'resolution_secs', 'accumulated', 'per_node', 'node_uids', 'param_param_key', 'no_zeroes', 'show_internal']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stats" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in params:
            query_params.append(('start_time', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('end_time', params['end_time']))  # noqa: E501
        if 'interval' in params:
            query_params.append(('interval', params['interval']))  # noqa: E501
        if 'category' in params:
            query_params.append(('category', params['category']))  # noqa: E501
            collection_formats['category'] = 'multi'  # noqa: E501
        if 'stat' in params:
            query_params.append(('stat', params['stat']))  # noqa: E501
            collection_formats['stat'] = 'multi'  # noqa: E501
        if 'resolution_secs' in params:
            query_params.append(('resolution_secs', params['resolution_secs']))  # noqa: E501
        if 'accumulated' in params:
            query_params.append(('accumulated', params['accumulated']))  # noqa: E501
        if 'per_node' in params:
            query_params.append(('per_node', params['per_node']))  # noqa: E501
        if 'node_uids' in params:
            query_params.append(('node_uids', params['node_uids']))  # noqa: E501
            collection_formats['node_uids'] = 'multi'  # noqa: E501
        if 'param_param_key' in params:
            query_params.append(('param[&lt;param_key&gt;][]', params['param_param_key']))  # noqa: E501
            collection_formats['param[&lt;param_key&gt;][]'] = 'multi'  # noqa: E501
        if 'no_zeroes' in params:
            query_params.append(('no_zeroes', params['no_zeroes']))  # noqa: E501
        if 'show_internal' in params:
            query_params.append(('show_internal', params['show_internal']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20075',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stats_description(self, **kwargs):  # noqa: E501
        """Get stats description  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stats_description(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20076
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_stats_description_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_stats_description_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_stats_description_with_http_info(self, **kwargs):  # noqa: E501
        """Get stats description  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stats_description_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20076
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
                    " to method get_stats_description" % key
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
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stats/description', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20076',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stats_disk_usage(self, **kwargs):  # noqa: E501
        """Get stats retention and estimated disk usage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stats_disk_usage(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str retention_duration: Duration (format - 1 minute 2 seconds, options - weeks, days, hours, minutes, seconds)
        :return: InlineResponse20078
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_stats_disk_usage_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_stats_disk_usage_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_stats_disk_usage_with_http_info(self, **kwargs):  # noqa: E501
        """Get stats retention and estimated disk usage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stats_disk_usage_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str retention_duration: Duration (format - 1 minute 2 seconds, options - weeks, days, hours, minutes, seconds)
        :return: InlineResponse20078
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['retention_duration']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stats_disk_usage" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'retention_duration' in params:
            query_params.append(('retention_duration', params['retention_duration']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stats/retention', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20078',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stats_retention(self, **kwargs):  # noqa: E501
        """Set stats retention  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stats_retention(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StatsRetentionBody body:
        :return: InlineResponse20078
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_stats_retention_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_stats_retention_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_stats_retention_with_http_info(self, **kwargs):  # noqa: E501
        """Set stats retention  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stats_retention_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StatsRetentionBody body:
        :return: InlineResponse20078
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stats_retention" % key
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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stats/retention', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20078',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
