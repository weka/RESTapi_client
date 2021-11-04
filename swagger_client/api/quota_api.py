# coding: utf-8

"""
    @weka-api

    <div>The Weka system supports a RESTful API. This is useful when automating the interaction with the Weka system and when integrating it into your workflows or monitoring systems. The API is accessible at port 14000, via the /api/v2 URL, you can explore it via /api/v2/docs when accessing from the cluster (e.g. https://weka01:14000/api/v2/docs).<div style=\"margin-top: 15px;\">Note: Weka uses 64bit numbers. Please take special care when interacting with the API with different program languages (In JS for example you can use \"json-bigint\")</div></div>  # noqa: E501

    OpenAPI spec version: 3.12.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class QuotaApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_quota(self, type, fs_uid, **kwargs):  # noqa: E501
        """Get file system quota  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_quota(type, fs_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: Quota type (required)
        :param str fs_uid: File system uid (required)
        :param str next_token: Token to get the next page
        :return: InlineResponse20045
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_quota_with_http_info(type, fs_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_quota_with_http_info(type, fs_uid, **kwargs)  # noqa: E501
            return data

    def get_quota_with_http_info(self, type, fs_uid, **kwargs):  # noqa: E501
        """Get file system quota  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_quota_with_http_info(type, fs_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: Quota type (required)
        :param str fs_uid: File system uid (required)
        :param str next_token: Token to get the next page
        :return: InlineResponse20045
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type', 'fs_uid', 'next_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_quota" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `get_quota`")  # noqa: E501
        # verify the required parameter 'fs_uid' is set
        if ('fs_uid' not in params or
                params['fs_uid'] is None):
            raise ValueError("Missing the required parameter `fs_uid` when calling `get_quota`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'fs_uid' in params:
            query_params.append(('fs_uid', params['fs_uid']))  # noqa: E501
        if 'next_token' in params:
            query_params.append(('next_token', params['next_token']))  # noqa: E501

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
            '/quota', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20045',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
